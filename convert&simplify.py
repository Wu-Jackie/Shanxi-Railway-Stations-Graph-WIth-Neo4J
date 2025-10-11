import csv
import json

# 输入文件名和输出文件名
input_file = '1.CSV'
output_file = '2.csv'

# 读取CSV文件并转换编码
with open(input_file, 'r', encoding='gb2312') as infile, open(output_file, 'w', encoding='utf-8',
                                                              newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

    # 写入表头
    writer.writeheader()

    # 处理每一行数据
    for row in reader:
        # 处理JSON格式的字符串
        for key in ['Type', 'TrainList']:
            try:
                # 将JSON字符串转换为列表
                data = json.loads(row[key])
                # 将列表转换为简单的字符串格式，用逗号分隔
                row[key] = ','.join(data)
            except json.JSONDecodeError:
                # 如果不是有效的JSON格式，保持原样
                pass

        # 写入处理后的行
        writer.writerow(row)

print(f"处理完成，结果已保存到 {output_file}")