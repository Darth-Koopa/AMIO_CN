import os

def split_binary_file(input_file, chunk_size=0xFF, output_prefix=""):
    """
    将二进制文件按指定大小分割成多个小文件
    
    参数:
        input_file: 输入文件名
        chunk_size: 每个小文件的大小，默认为0xFF(255)字节
        output_prefix: 输出文件前缀
    """
    try:
        # 检查输入文件是否存在
        if not os.path.exists(input_file):
            print(f"错误: 文件 '{input_file}' 不存在")
            return
        
        # 打开输入文件
        with open(input_file, 'rb') as f:
            chunk_number = 1
            while True:
                # 读取指定大小的数据
                chunk = f.read(chunk_size)
                
                # 如果读取到的数据为空，说明已经到文件末尾
                if not chunk:
                    break
                
                # 生成输出文件名，格式为0001.mio, 0002.mio等
                output_filename = f"{output_prefix}{chunk_number:04d}.mio"
                
                # 写入到新文件
                with open(output_filename, 'wb') as out_f:
                    out_f.write(chunk)
                
                print(f"已生成: {output_filename}")
                chunk_number += 1
        
        print(f"分割完成，共生成 {chunk_number - 1} 个文件")
        
    except Exception as e:
        print(f"处理过程中发生错误: {str(e)}")

if __name__ == "__main__":
    # 分割11.bin文件，每0xFF字节一个文件，输出文件名为0001.mio, 0002.mio...
    split_binary_file("M.decomp.bin_l", 0x3800, "")
    
