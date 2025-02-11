# 删除dat文件中符合特定条件的行

# 中国境内的判断列表
china_areas = {'ZB', 'ZG', 'ZY', 'ZS', 'ZW', 'ZJ', 'ZP', 'ZL', 'ZH', 'ZU'}

# 原始文件路径
input_file = '/Users/lujuncheng/Downloads/xplane12_native_2501/earth_awy.dat'
# 输出文件路径
output_file = '/Users/lujuncheng/Downloads/PMDG NavData/earth_awy_6643.dat'

try:
    with open(input_file, 'r', encoding='utf-8') as file_input:
        with open(output_file, 'w', encoding='utf-8') as file_output:
            for line in file_input:
                # 删除换行符，并按空格分隔
                parts = line.strip().split()
                # 检查是否有11个部分
                if len(parts) != 11:
                    continue  # 跳过不完整的行
                # 获取第二和第五部分
                part2 = parts[1]
                part5 = parts[4]
                # 判断是否在中国境内
                if part2 in china_areas and part5 in china_areas:
                    continue  # 删除该行
                # 如果不符合条件，写入输出文件
                file_output.write(line)
    print("处理完成！已将符合条件的行删除，结果保存在output.dat中。")
except FileNotFoundError:
    print("文件未找到，请检查输入文件路径是否正确。")
except Exception as e:
    print(f"发生错误：{e}")
