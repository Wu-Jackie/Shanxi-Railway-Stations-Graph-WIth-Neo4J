def process_csv_with_quotes(input_file, output_file, target_str, prefix_str):
    try:
        with open(input_file, mode='r', encoding='utf-8') as infile, \
                open(output_file, mode='w', encoding='utf-8') as outfile:

            for line in infile:
                # 去除行尾的换行符，但保留其他格式
                stripped_line = line.rstrip('\n')

                # 检查当前行是否包含目标字符串
                if target_str in stripped_line:
                    # 在查找到的字符串两侧添加单引号
                    modified_line = stripped_line.replace(target_str, f"'{target_str}'")
                    # 在符合条件的行前追加前缀字符串，直接拼接
                    new_line = f"{prefix_str}{modified_line}"
                else:
                    # 不符合条件的行保持不变
                    new_line = stripped_line

                # 写入处理后的行，并添加换行符
                outfile.write(f"{new_line}\n")

        print(f"处理完成，结果已保存至 {output_file}")

    except FileNotFoundError:
        print(f"错误: 找不到文件 {input_file}")
    except Exception as e:
        print(f"处理过程中发生错误: {str(e)}")


# 使用示例
if __name__ == "__main__":
    # 输入文件路径
    input_csv = "2.csv"
    # 输出文件路径
    output_csv = "1.csv"
    # 要查找的字符串a
    str_a = "D1049"
    # 要追加的字符串b
    str_b = "/28"

    # 调用函数处理CSV
    process_csv_with_quotes(input_csv, output_csv, str_a, str_b)
