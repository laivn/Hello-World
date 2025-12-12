#!/usr/bin/env python3
import sys

def convert_to_clash(input_file, output_file, policy="DIRECT"):
    """
    将IPv6列表转换为Clash兼容格式
    
    Args:
        input_file: 输入文件路径
        output_file: 输出文件路径
        policy: 策略名称，默认为DIRECT
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        converted_lines = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 原始格式: IP-CIDR6,2001:250::/30
            # Clash格式: IP-CIDR6,2001:250::/30,DIRECT
            if line.startswith('IP-CIDR6,'):
                # 直接添加策略
                clash_line = f"{line},{policy}"
                converted_lines.append(clash_line)
            else:
                # 如果不是IP-CIDR6开头，可能是其他格式，保持原样
                converted_lines.append(line)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(converted_lines))
        
        print(f"转换完成！共处理 {len(converted_lines)} 条规则")
        print(f"输出文件: {output_file}")
        
    except Exception as e:
        print(f"转换出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法: python convert_ipv6_to_clash.py <输入文件> [输出文件] [策略]")
        print("示例: python convert_ipv6_to_clash.py IPv6.list IPv6-clash.list DIRECT")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "IPv6-clash.list"
    policy = sys.argv[3] if len(sys.argv) > 3 else "DIRECT"
    
    convert_to_clash(input_file, output_file, policy)