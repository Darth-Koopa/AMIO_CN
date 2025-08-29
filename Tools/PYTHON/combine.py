import os
import re

def merge_bin_files(folder_path, output_file="out.bin"):
    """
    将文件夹中的bin文件按序号从小到大合并为一个文件
    
    参数:
        folder_path: bin文件所在的文件夹路径
        output_file: 输出文件的名称，默认为"out.bin"
    """
    # 确保文件夹路径存在
    if not os.path.exists(folder_path):
        print(f"错误: 文件夹 '{folder_path}' 不存在")
        return
    
    # 获取文件夹中所有bin文件
    bin_files = []
    for filename in os.listdir(folder_path):
        # 匹配类似0002.bin的文件名
        match = re.match(r'^(\d+)\.mio$', filename)
        if match:
            # 提取序号并转换为整数
            try:
                number = int(match.group(1))
                bin_files.append((number, filename))
            except ValueError:
                # 如果无法转换为整数，跳过该文件
                continue
    
    if not bin_files:
        print("未找到任何bin文件")
        return
    
    # 按序号排序
    bin_files.sort(key=lambda x: x[0])
    print(f"找到{len(bin_files)}个bin文件，将按以下顺序合并:")
    for num, filename in bin_files:
        print(f"  {filename}")
    
    # 合并文件
    output_path = os.path.join(folder_path, output_file)
    try:
        with open(output_path, 'wb') as outfile:
            for num, filename in bin_files:
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'rb') as infile:
                    # 读取并写入文件内容
                    outfile.write(infile.read())
        print(f"文件合并完成，输出文件: {output_path}")
    except Exception as e:
        print(f"合并文件时出错: {str(e)}")

if __name__ == "__main__":
    # 可以在这里修改文件夹路径
    target_folder = "."  # 默认当前目录下的bin_files文件夹
    
    # 如果文件夹不存在则创建
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"创建了文件夹: {target_folder}")
        print("请将bin文件放入该文件夹后重新运行程序")
    else:
        merge_bin_files(target_folder)
    
