import os

def extract_and_merge(folder_path, start_offset=0x90, end_offset=0xA0, output_file="result.bin"):
    """
    提取文件夹内所有bin文件的指定范围字节，并合并到一个文件中
    
    参数:
        folder_path: 包含bin文件的文件夹路径
        start_offset: 起始偏移量（十六进制），默认为0x90
        end_offset: 结束偏移量（十六进制），默认为0xA0
        output_file: 输出的合并文件名
    """
    try:
        # 检查文件夹是否存在
        if not os.path.isdir(folder_path):
            print(f"错误: 文件夹 '{folder_path}' 不存在")
            return
        
        # 计算需要提取的字节数
        bytes_to_extract = end_offset - start_offset + 1  # 包含起始和结束位置
        print(f"将提取每个文件从0x{start_offset:X}到0x{end_offset:X}的字节，共{bytes_to_extract}字节")
        
        # 获取文件夹内所有.bin文件
        bin_files = [f for f in os.listdir(folder_path) 
                    if f.lower().endswith('.mio') and os.path.isfile(os.path.join(folder_path, f))]
        
        if not bin_files:
            print(f"警告: 在文件夹 '{folder_path}' 中未找到任何bin文件")
            return
        
        # 按文件名排序，确保处理顺序一致
        bin_files.sort()
        
        # 打开输出文件准备写入
        with open(output_file, 'wb') as out_f:
            for file_name in bin_files:
                file_path = os.path.join(folder_path, file_name)
                try:
                    with open(file_path, 'rb') as in_f:
                        # 移动到起始偏移量
                        in_f.seek(start_offset)
                        # 读取指定范围的字节
                        data = in_f.read(bytes_to_extract)
                        # 写入到输出文件
                        out_f.write(data)
                        print(f"已提取: {file_name} (实际读取{len(data)}字节)")
                except Exception as e:
                    print(f"处理文件 {file_name} 时出错: {str(e)}")
        
        print(f"\n合并完成，结果已保存到 {output_file}")
        print(f"共处理 {len(bin_files)} 个bin文件")
        
    except Exception as e:
        print(f"处理过程中发生错误: {str(e)}")

if __name__ == "__main__":
    # 处理当前目录下的所有bin文件，提取0x90到0xA0范围的字节
    extract_and_merge(".", 0x1c, 0x47)
    
