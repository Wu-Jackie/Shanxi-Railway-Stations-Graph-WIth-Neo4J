# Shanxi's Railway Stations Graph WIth Neo4J

- Neo4J：[Neo4J 5.26.12 Community Edition](https://neo4j.com/deployment-center/)

# 数据获取

[RailGo.Parser](https://github.com/AZ-Studio-2023/RailGo.Parser)

> 需本地有MongoDB、SQLite

如果是初次下载SQLite，在该项目mongo_sqlite.py文件clear函数添加相关代码

```python
import os

def clear(self):
    # 确保数据库文件所在的目录存在
    if not os.path.exists(os.path.dirname(self.export_location)):
        os.makedirs(os.path.dirname(self.export_location))
# 上两位代码为新增
    super().clear()
    db = sqlite3.connect(self.export_location)
    # 后面代码省略...
```

数据生成在export文件夹，利用Navicat查询导出

```sqlite
SELECT COUNT(*) FROM "main"."stations";--COUNT(*)=8355
SELECT * FROM "man"."stations" WHERE province='山西省';
```

# 数据处理

1. Navicat导出xlsx，利用[RailGo](https://github.com/AZ-Studio-2023/RailGo)、[rail.re](https://rail.re/)等补全信息，本Repo以小部分车站为例，删去了无车次的车站

2. xlsx导出为csv后转换编码GB2312为UTF\-8（注意车站生僻字）、简化字符串格式（Type和TrainList）

   > 参考[convert&simplify.py](https://github.com/Wu-Jackie/Shanxi-Railway-Stations-Graph-WIth-Neo4J/blob/main/convert%26simplify.py)

3. 以小部分车次数据为例，此时需标记需要的车次并清洗无关数据得到Stations.csv

   > 参考[mark.py](https://github.com/Wu-Jackie/Shanxi-Railway-Stations-Graph-WIth-Neo4J/blob/main/mark.py)
   >
   > 保留的车次详见[Create relationship.md](https://github.com/Wu-Jackie/Shanxi-Railway-Stations-Graph-WIth-Neo4J/blob/main/Create%20relationship.md)目录

Stations.csv放在Neo4J安装目录的import文件夹

# Neo4J

```
neo4j console
```

## 节点

### 创建节点举例

```cypher
create (n:Person{name:'Jackie',title:'Manager'}) return n

CREATE (s:Station {
  Name: 北舍,
  Pinyin: Beishe,
  Telecode: BNP,
  PinyinTriple: BSH,
  TMIS: 21581,
  Bureau: 北京局,
  City: 长治市,
  Type: 货,客
})
```

### 批量创建节点

```cypher
LOAD CSV WITH HEADERS FROM 'file:///Stations.csv' AS row
CREATE (s:Station {
  Name: row.Name,
  Pinyin: row.Pinyin,
  Telecode: row.Telecode,
  PinyinTriple: row.PinyinTriple,
  TMIS: row.TMIS,
  Bureau: row.Bureau,
  City: row.City,
  Type: row.Type
})
```

### 删除所有节点

```cypher
MATCH (n)
DETACH DELETE n
```

### 删除节点

```cypher
//DETACH DELETE确保删除节点前先删除与该节点相关的所有关系
MATCH (n {Name: "北舍"})
DETACH DELETE n
```

### 更改节点属性

```cypher
MATCH (s:Station {Name: '北舍'})
SET s.Type = '货,客,高'
RETURN s
```

### 按条件查询节点

```cypher
//查找太原市的所有车站
MATCH (n {City: "太原市"})
RETURN n
//查找所有与"北舍"节点有关系的节点
MATCH (n {Name: "北舍"})-[]-(related)
RETURN n,related
```

## 关系

### 创建关系

```cypher
MATCH (s1:Station {Name: '南山交'}), (s2:Station {Name: '东阳关'})
CREATE (s1)-[:`6043`]->(s2)
```

详细在[Create relationship.md](https://github.com/Wu-Jackie/Shanxi-Railway-Stations-Graph-WIth-Neo4J/blob/main/Create%20relationship.md)中

### 删除关系

```cypher
MATCH (s1:Station {Name: '南山交'})-[:`6043`]->(s2:Station {Name: '东阳关'})
DELETE s1-[:`6043`]->s2
```

### 查询所有有关系的节点

```cypher
//查询所有有关系的节点
MATCH (s1:Station)-[r]->(s2:Station)
RETURN s1, r, s2
```

### 查询所有没有关系的节点

```cypher
MATCH (s:Station)
WHERE NOT (s)--()
RETURN s
```

### 查询6043车次经过的车站

```cypher
MATCH (s1:Station)-[r:`6043`]->(s2:Station)
RETURN s1, r, s2
```

# 导出数据库

```powershell
neo4j-admin database dump --to-path="D:\Database" neo4j
```
