# 6043

```cypher
MATCH (s1:Station {Name: '南山交'}), (s2:Station {Name: '东阳关'})
CREATE (s1)-[:`6043`]->(s2)

MATCH (s1:Station {Name: '东阳关'}), (s2:Station {Name: '黎城'})
CREATE (s1)-[:`6043`]->(s2)

MATCH (s1:Station {Name: '黎城'}), (s2:Station {Name: '水洋'})
CREATE (s1)-[:`6043`]->(s2)

MATCH (s1:Station {Name: '水洋'}), (s2:Station {Name: '常村'})
CREATE (s1)-[:`6043`]->(s2)

MATCH (s1:Station {Name: '常村'}), (s2:Station {Name: '漫流河'})
CREATE (s1)-[:`6043`]->(s2)

MATCH (s1:Station {Name: '漫流河'}), (s2:Station {Name: '微子镇'})
CREATE (s1)-[:`6043`]->(s2)

MATCH (s1:Station {Name: '微子镇'}), (s2:Station {Name: '潞城'})
CREATE (s1)-[:`6043`]->(s2)

MATCH (s1:Station {Name: '潞城'}), (s2:Station {Name: '北舍'})
CREATE (s1)-[:`6043`]->(s2)

MATCH (s1:Station {Name: '北舍'}), (s2:Station {Name: '长治北'})
CREATE (s1)-[:`6043`]->(s2)
```

- 查询

```cypher
MATCH (s1:Station)-[r:`6043`]->(s2:Station)
RETURN s1, r, s2
```

## 6044

```cypher
MATCH (s1:Station {Name: '长治北'}), (s2:Station {Name: '北舍'})
CREATE (s1)-[:`6044`]->(s2)

MATCH (s1:Station {Name: '北舍'}), (s2:Station {Name: '潞城'})
CREATE (s1)-[:`6044`]->(s2)

MATCH (s1:Station {Name: '潞城'}), (s2:Station {Name: '微子镇'})
CREATE (s1)-[:`6044`]->(s2)

MATCH (s1:Station {Name: '微子镇'}), (s2:Station {Name: '漫流河'})
CREATE (s1)-[:`6044`]->(s2)

MATCH (s1:Station {Name: '漫流河'}), (s2:Station {Name: '常村'})
CREATE (s1)-[:`6044`]->(s2)

MATCH (s1:Station {Name: '常村'}), (s2:Station {Name: '水洋'})
CREATE (s1)-[:`6044`]->(s2)

MATCH (s1:Station {Name: '水洋'}), (s2:Station {Name: '黎城'})
CREATE (s1)-[:`6044`]->(s2)

MATCH (s1:Station {Name: '黎城'}), (s2:Station {Name: '东阳关'})
CREATE (s1)-[:`6044`]->(s2)

MATCH (s1:Station {Name: '东阳关'}), (s2:Station {Name: '南山交'})
CREATE (s1)-[:`6044`]->(s2)
```

# 6438

```cypher
MATCH (s1:Station {Name: '大涧'}), (s2:Station {Name: '云彩岭'})
CREATE (s1)-[:`6438`]->(s2)

MATCH (s1:Station {Name: '云彩岭'}), (s2:Station {Name: '招柏'})
CREATE (s1)-[:`6438`]->(s2)
```

## 6437

```cypher
MATCH (s1:Station {Name: '招柏'}), (s2:Station {Name: '云彩岭'})
CREATE (s1)-[:`6437`]->(s2)

MATCH (s1:Station {Name: '云彩岭'}), (s2:Station {Name: '大涧'})
CREATE (s1)-[:`6437`]->(s2)
```

# K4588

```cypher
MATCH (s1:Station {Name: '左权'}), (s2:Station {Name: '和顺县'})
CREATE (s1)-[:`K4588`]->(s2)

MATCH (s1:Station {Name: '和顺县'}), (s2:Station {Name: '昔阳'})
CREATE (s1)-[:`K4588`]->(s2)

MATCH (s1:Station {Name: '昔阳'}), (s2:Station {Name: '平定'})
CREATE (s1)-[:`K4588`]->(s2)

MATCH (s1:Station {Name: '平定'}), (s2:Station {Name: '阳泉东'})
CREATE (s1)-[:`K4588`]->(s2)

MATCH (s1:Station {Name: '阳泉东'}), (s2:Station {Name: '阳泉北'})
CREATE (s1)-[:`K4588`]->(s2)

MATCH (s1:Station {Name: '阳泉北'}), (s2:Station {Name: '太原'})
CREATE (s1)-[:`K4588`]->(s2)
```

## K4586

```cypher
MATCH (s1:Station {Name: '太原'}), (s2:Station {Name: '阳泉北'})
CREATE (s1)-[:`K4586`]->(s2)

MATCH (s1:Station {Name: '阳泉北'}), (s2:Station {Name: '阳泉东'})
CREATE (s1)-[:`K4586`]->(s2)

MATCH (s1:Station {Name: '阳泉东'}), (s2:Station {Name: '平定'})
CREATE (s1)-[:`K4586`]->(s2)

MATCH (s1:Station {Name: '平定'}), (s2:Station {Name: '昔阳'})
CREATE (s1)-[:`K4586`]->(s2)

MATCH (s1:Station {Name: '昔阳'}), (s2:Station {Name: '和顺县'})
CREATE (s1)-[:`K4586`]->(s2)

MATCH (s1:Station {Name: '和顺县'}), (s2:Station {Name: '左权'})
CREATE (s1)-[:`K4586`]->(s2)
```

# 6055

```cypher
MATCH (s1:Station {Name: '大同'}), (s2:Station {Name: '孤山'})
CREATE (s1)-[:`6055`]->(s2)

MATCH (s1:Station {Name: '孤山'}), (s2:Station {Name: '堡子湾'})
CREATE (s1)-[:`6055`]->(s2)
```

## 6056

```cypher
MATCH (s1:Station {Name: '堡子湾'}), (s2:Station {Name: '孤山'})
CREATE (s1)-[:`6056`]->(s2)

MATCH (s1:Station {Name: '孤山'}), (s2:Station {Name: '大同'})
CREATE (s1)-[:`6056`]->(s2)
```

# K903（高平只有K903）

```cypher
MATCH (s1:Station {Name: '太原'}), (s2:Station {Name: '榆次'})
CREATE (s1)-[:`K903`]->(s2)

MATCH (s1:Station {Name: '榆次'}), (s2:Station {Name: '榆社'})
CREATE (s1)-[:`K903`]->(s2)

MATCH (s1:Station {Name: '榆社'}), (s2:Station {Name: '武乡东'})
CREATE (s1)-[:`K903`]->(s2)

MATCH (s1:Station {Name: '武乡东'}), (s2:Station {Name: '沁县'})
CREATE (s1)-[:`K903`]->(s2)

MATCH (s1:Station {Name: '沁县'}), (s2:Station {Name: '襄垣'})
CREATE (s1)-[:`K903`]->(s2)

MATCH (s1:Station {Name: '襄垣'}), (s2:Station {Name: '长治北'})
CREATE (s1)-[:`K903`]->(s2)

MATCH (s1:Station {Name: '长治北'}), (s2:Station {Name: '长治'})
CREATE (s1)-[:`K903`]->(s2)

MATCH (s1:Station {Name: '长治'}), (s2:Station {Name: '高平'})
CREATE (s1)-[:`K903`]->(s2)

MATCH (s1:Station {Name: '高平'}), (s2:Station {Name: '晋城'})
CREATE (s1)-[:`K903`]->(s2)
```

## K901

```cypher
MATCH (s1:Station {Name: '晋城'}), (s2:Station {Name: '长治'})
CREATE (s1)-[:`K901`]->(s2)

MATCH (s1:Station {Name: '长治'}), (s2:Station {Name: '长治北'})
CREATE (s1)-[:`K901`]->(s2)

MATCH (s1:Station {Name: '长治北'}), (s2:Station {Name: '襄垣'})
CREATE (s1)-[:`K901`]->(s2)

MATCH (s1:Station {Name: '襄垣'}), (s2:Station {Name: '沁县'})
CREATE (s1)-[:`K901`]->(s2)

MATCH (s1:Station {Name: '沁县'}), (s2:Station {Name: '武乡东'})
CREATE (s1)-[:`K901`]->(s2)

MATCH (s1:Station {Name: '武乡东'}), (s2:Station {Name: '榆社'})
CREATE (s1)-[:`K901`]->(s2)

MATCH (s1:Station {Name: '榆社'}), (s2:Station {Name: '榆次'})
CREATE (s1)-[:`K901`]->(s2)

MATCH (s1:Station {Name: '榆次'}), (s2:Station {Name: '太原'})
CREATE (s1)-[:`K901`]->(s2)
```

# 4616

```cypher
MATCH (s1:Station {Name: '太原'}), (s2:Station {Name: '阳曲'})
CREATE (s1)-[:`4616`]->(s2)

MATCH (s1:Station {Name: '阳曲'}), (s2:Station {Name: '忻州'})
CREATE (s1)-[:`4616`]->(s2)

MATCH (s1:Station {Name: '忻州'}), (s2:Station {Name: '原平'})
CREATE (s1)-[:`4616`]->(s2)

MATCH (s1:Station {Name: '原平'}), (s2:Station {Name: '轩岗'})
CREATE (s1)-[:`4616`]->(s2)

MATCH (s1:Station {Name: '轩岗'}), (s2:Station {Name: '宁武'})
CREATE (s1)-[:`4616`]->(s2)

MATCH (s1:Station {Name: '宁武'}), (s2:Station {Name: '神池'})
CREATE (s1)-[:`4616`]->(s2)

MATCH (s1:Station {Name: '神池'}), (s2:Station {Name: '五寨'})
CREATE (s1)-[:`4616`]->(s2)

MATCH (s1:Station {Name: '五寨'}), (s2:Station {Name: '安塘'})
CREATE (s1)-[:`4616`]->(s2)

MATCH (s1:Station {Name: '安塘'}), (s2:Station {Name: '秦家庄'})
CREATE (s1)-[:`4616`]->(s2)

MATCH (s1:Station {Name: '秦家庄'}), (s2:Station {Name: '岢岚'})
CREATE (s1)-[:`4616`]->(s2)
```

## 4618

```cypher
MATCH (s1:Station {Name: '岢岚'}), (s2:Station {Name: '秦家庄'})
CREATE (s1)-[:`4618`]->(s2)

MATCH (s1:Station {Name: '秦家庄'}), (s2:Station {Name: '安塘'})
CREATE (s1)-[:`4618`]->(s2)

MATCH (s1:Station {Name: '安塘'}), (s2:Station {Name: '五寨'})
CREATE (s1)-[:`4618`]->(s2)

MATCH (s1:Station {Name: '五寨'}), (s2:Station {Name: '神池'})
CREATE (s1)-[:`4618`]->(s2)

MATCH (s1:Station {Name: '神池'}), (s2:Station {Name: '宁武'})
CREATE (s1)-[:`4618`]->(s2)

MATCH (s1:Station {Name: '宁武'}), (s2:Station {Name: '轩岗'})
CREATE (s1)-[:`4618`]->(s2)

MATCH (s1:Station {Name: '轩岗'}), (s2:Station {Name: '原平'})
CREATE (s1)-[:`4618`]->(s2)

MATCH (s1:Station {Name: '原平'}), (s2:Station {Name: '忻州'})
CREATE (s1)-[:`4618`]->(s2)

MATCH (s1:Station {Name: '忻州'}), (s2:Station {Name: '阳曲'})
CREATE (s1)-[:`4618`]->(s2)

MATCH (s1:Station {Name: '阳曲'}), (s2:Station {Name: '太原'})
CREATE (s1)-[:`4618`]->(s2)
```

# K2095

```cypher
MATCH (s1:Station {Name: '大同'}), (s2:Station {Name: '怀仁东'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '怀仁东'}), (s2:Station {Name: '应县'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '应县'}), (s2:Station {Name: '山阴'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '山阴'}), (s2:Station {Name: '原平'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '原平'}), (s2:Station {Name: '忻州'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '忻州'}), (s2:Station {Name: '太原'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '太原'}), (s2:Station {Name: '太原南'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '太原南'}), (s2:Station {Name: '榆次'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '榆次'}), (s2:Station {Name: '太谷'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '太谷'}), (s2:Station {Name: '祁县'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '祁县'}), (s2:Station {Name: '平遥'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '平遥'}), (s2:Station {Name: '介休'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '介休'}), (s2:Station {Name: '临汾'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '临汾'}), (s2:Station {Name: '侯马'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '侯马'}), (s2:Station {Name: '稷山'})
CREATE (s1)-[:`K2095`]->(s2)

MATCH (s1:Station {Name: '稷山'}), (s2:Station {Name: '河津'})
CREATE (s1)-[:`K2095`]->(s2)
```

## K2096

```cypher
MATCH (s1:Station {Name: '河津'}), (s2:Station {Name: '稷山'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '稷山'}), (s2:Station {Name: '侯马'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '侯马'}), (s2:Station {Name: '临汾'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '临汾'}), (s2:Station {Name: '介休'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '介休'}), (s2:Station {Name: '平遥'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '平遥'}), (s2:Station {Name: '祁县'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '祁县'}), (s2:Station {Name: '太谷'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '太谷'}), (s2:Station {Name: '榆次'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '榆次'}), (s2:Station {Name: '太原南'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '太原南'}), (s2:Station {Name: '太原'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '太原'}), (s2:Station {Name: '忻州'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '忻州'}), (s2:Station {Name: '原平'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '原平'}), (s2:Station {Name: '山阴'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '山阴'}), (s2:Station {Name: '应县'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '应县'}), (s2:Station {Name: '怀仁东'})
CREATE (s1)-[:`K2096`]->(s2)

MATCH (s1:Station {Name: '怀仁东'}), (s2:Station {Name: '大同'})
CREATE (s1)-[:`K2096`]->(s2)
```

# K603

```cypher
MATCH (s1:Station {Name: '灵丘'}), (s2:Station {Name: '五台山'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '五台山'}), (s2:Station {Name: '繁峙'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '繁峙'}), (s2:Station {Name: '代县'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '代县'}), (s2:Station {Name: '原平'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '原平'}), (s2:Station {Name: '忻州'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '忻州'}), (s2:Station {Name: '太原'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '太原'}), (s2:Station {Name: '榆次'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '榆次'}), (s2:Station {Name: '太谷'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '太谷'}), (s2:Station {Name: '祁县'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '祁县'}), (s2:Station {Name: '平遥'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '平遥'}), (s2:Station {Name: '介休'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '介休'}), (s2:Station {Name: '霍州'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '霍州'}), (s2:Station {Name: '临汾'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '临汾'}), (s2:Station {Name: '襄汾'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '襄汾'}), (s2:Station {Name: '侯马'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '侯马'}), (s2:Station {Name: '东镇'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '东镇'}), (s2:Station {Name: '闻喜'})
CREATE (s1)-[:`K603`]->(s2)

MATCH (s1:Station {Name: '闻喜'}), (s2:Station {Name: '运城'})
CREATE (s1)-[:`K603`]->(s2)
```

## K604

```cypher
MATCH (s1:Station {Name: '运城'}), (s2:Station {Name: '闻喜'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '闻喜'}), (s2:Station {Name: '东镇'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '东镇'}), (s2:Station {Name: '侯马'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '侯马'}), (s2:Station {Name: '襄汾'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '襄汾'}), (s2:Station {Name: '临汾'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '临汾'}), (s2:Station {Name: '霍州'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '霍州'}), (s2:Station {Name: '介休'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '介休'}), (s2:Station {Name: '平遥'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '平遥'}), (s2:Station {Name: '祁县'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '祁县'}), (s2:Station {Name: '太谷'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '太谷'}), (s2:Station {Name: '榆次'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '榆次'}), (s2:Station {Name: '太原'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '太原'}), (s2:Station {Name: '忻州'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '忻州'}), (s2:Station {Name: '原平'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '原平'}), (s2:Station {Name: '代县'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '代县'}), (s2:Station {Name: '繁峙'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '繁峙'}), (s2:Station {Name: '五台山'})
CREATE (s1)-[:`K604`]->(s2)

MATCH (s1:Station {Name: '五台山'}), (s2:Station {Name: '灵丘'})
CREATE (s1)-[:`K604`]->(s2)
```

# Z9206

```cypher
MATCH (s1:Station {Name: '柳林南'}), (s2:Station {Name: '吕梁'})
CREATE (s1)-[:`Z9206`]->(s2)

MATCH (s1:Station {Name: '吕梁'}), (s2:Station {Name: '汾阳'})
CREATE (s1)-[:`Z9206`]->(s2)

MATCH (s1:Station {Name: '汾阳'}), (s2:Station {Name: '文水'})
CREATE (s1)-[:`Z9206`]->(s2)

MATCH (s1:Station {Name: '文水'}), (s2:Station {Name: '交城'})
CREATE (s1)-[:`Z9206`]->(s2)

MATCH (s1:Station {Name: '交城'}), (s2:Station {Name: '太原'})
CREATE (s1)-[:`Z9206`]->(s2)
```

# G622

```cypher
MATCH (s1:Station {Name: '运城北'}), (s2:Station {Name: '闻喜西'})
CREATE (s1)-[:`G622`]->(s2)

MATCH (s1:Station {Name: '闻喜西'}), (s2:Station {Name: '侯马西'})
CREATE (s1)-[:`G622`]->(s2)

MATCH (s1:Station {Name: '侯马西'}), (s2:Station {Name: '临汾西'})
CREATE (s1)-[:`G622`]->(s2)

MATCH (s1:Station {Name: '临汾西'}), (s2:Station {Name: '灵石东'})
CREATE (s1)-[:`G622`]->(s2)

MATCH (s1:Station {Name: '灵石东'}), (s2:Station {Name: '介休东'})
CREATE (s1)-[:`G622`]->(s2)

MATCH (s1:Station {Name: '介休东'}), (s2:Station {Name: '太谷西'})
CREATE (s1)-[:`G622`]->(s2)

MATCH (s1:Station {Name: '太谷西'}), (s2:Station {Name: '太原南'})
CREATE (s1)-[:`G622`]->(s2)

MATCH (s1:Station {Name: '太原南'}), (s2:Station {Name: '太原'})
CREATE (s1)-[:`G622`]->(s2)

MATCH (s1:Station {Name: '太原'}), (s2:Station {Name: '阳泉北'})
CREATE (s1)-[:`G622`]->(s2)
```

# G623

```cypher
MATCH (s1:Station {Name: '阳泉北'}), (s2:Station {Name: '太原南'})
CREATE (s1)-[:`G623`]->(s2)

MATCH (s1:Station {Name: '太原南'}), (s2:Station {Name: '晋中'})
CREATE (s1)-[:`G623`]->(s2)

MATCH (s1:Station {Name: '晋中'}), (s2:Station {Name: '太谷西'})
CREATE (s1)-[:`G623`]->(s2)

MATCH (s1:Station {Name: '太谷西'}), (s2:Station {Name: '襄汾西'})
CREATE (s1)-[:`G623`]->(s2)

MATCH (s1:Station {Name: '襄汾西'}), (s2:Station {Name: '闻喜西'})
CREATE (s1)-[:`G623`]->(s2)

MATCH (s1:Station {Name: '闻喜西'}), (s2:Station {Name: '运城北'})
CREATE (s1)-[:`G623`]->(s2)
```

# G2405

```cypher
MATCH (s1:Station {Name: '大同南'}), (s2:Station {Name: '怀仁东'})
CREATE (s1)-[:`G2405`]->(s2)

MATCH (s1:Station {Name: '怀仁东'}), (s2:Station {Name: '山阴南'})
CREATE (s1)-[:`G2405`]->(s2)

MATCH (s1:Station {Name: '山阴南'}), (s2:Station {Name: '朔州东'})
CREATE (s1)-[:`G2405`]->(s2)

MATCH (s1:Station {Name: '朔州东'}), (s2:Station {Name: '原平西'})
CREATE (s1)-[:`G2405`]->(s2)

MATCH (s1:Station {Name: '原平西'}), (s2:Station {Name: '忻州西'})
CREATE (s1)-[:`G2405`]->(s2)

MATCH (s1:Station {Name: '忻州西'}), (s2:Station {Name: '阳曲西'})
CREATE (s1)-[:`G2405`]->(s2)

MATCH (s1:Station {Name: '阳曲西'}), (s2:Station {Name: '太原南'})
CREATE (s1)-[:`G2405`]->(s2)

MATCH (s1:Station {Name: '太原南'}), (s2:Station {Name: '榆社西'})
CREATE (s1)-[:`G2405`]->(s2)

MATCH (s1:Station {Name: '榆社西'}), (s2:Station {Name: '襄垣东'})
CREATE (s1)-[:`G2405`]->(s2)

MATCH (s1:Station {Name: '襄垣东'}), (s2:Station {Name: '长治东'})
CREATE (s1)-[:`G2405`]->(s2)

MATCH (s1:Station {Name: '长治东'}), (s2:Station {Name: '长治南'})
CREATE (s1)-[:`G2405`]->(s2)

MATCH (s1:Station {Name: '长治南'}), (s2:Station {Name: '高平东'})
CREATE (s1)-[:`G2405`]->(s2)

MATCH (s1:Station {Name: '高平东'}), (s2:Station {Name: '晋城东'})
CREATE (s1)-[:`G2405`]->(s2)
```

# D1049

```cypher
MATCH (s1:Station {Name: '大同南'}), (s2:Station {Name: '应县西'})
CREATE (s1)-[:`D1049`]->(s2)

MATCH (s1:Station {Name: '应县西'}), (s2:Station {Name: '朔州东'})
CREATE (s1)-[:`D1049`]->(s2)

MATCH (s1:Station {Name: '朔州东'}), (s2:Station {Name: '雁门关'})
CREATE (s1)-[:`D1049`]->(s2)

MATCH (s1:Station {Name: '雁门关'}), (s2:Station {Name: '忻州西'})
CREATE (s1)-[:`D1049`]->(s2)

MATCH (s1:Station {Name: '忻州西'}), (s2:Station {Name: '太原南'})
CREATE (s1)-[:`D1049`]->(s2)

MATCH (s1:Station {Name: '太原南'}), (s2:Station {Name: '祁县东'})
CREATE (s1)-[:`D1049`]->(s2)

MATCH (s1:Station {Name: '祁县东'}), (s2:Station {Name: '介休东'})
CREATE (s1)-[:`D1049`]->(s2)

MATCH (s1:Station {Name: '介休东'}), (s2:Station {Name: '洪洞西'})
CREATE (s1)-[:`D1049`]->(s2)

MATCH (s1:Station {Name: '洪洞西'}), (s2:Station {Name: '闻喜西'})
CREATE (s1)-[:`D1049`]->(s2)

MATCH (s1:Station {Name: '闻喜西'}), (s2:Station {Name: '运城北'})
CREATE (s1)-[:`D1049`]->(s2)
```

