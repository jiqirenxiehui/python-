#!/usr/bin/env python
# -*- coding: utf-8 -*-

#统计LINUX 登录日志出现的IP地址次数
import re                                                                                
def count_and_sort_ip_in_log(file_path):
    try:
        ip_counts = {} #创建保存数据的字典
        with open(file_path, 'r', encoding='utf-8') as file:
            content=file.readline()
            while content:                                                                                                                                
                
                #ip_adress=re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', content)  #匹配IP
                ip_adress=re.findall(r'sa=\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', content) #匹配sa=的源IP地址，根据自己需要的写正则表达式
                #ip_adress=re.findall(r'sport=\d{1,5}', content)  #匹配端口

                if ip_adress:                                                                                                                                
                    sa_ip = str(ip_adress[0]) #得到sa=的源IP地址
                    ip=sa_ip[3:] #得到源IP地址,切割数据                                                                                                                                
                    if ip not in ip_counts:
                        ip_counts[ip] = 1                                                                                                                                
                    else:                                                                                                                                
                        ip_counts[ip] += 1                                                                                                                                
                content=file.readline()
        sorted_ip_counts = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
        print(f"IP 地址\t\t出现次数\t 一共出现{len(sorted_ip_counts)}个不同的IP地址")
        print("-----------------------")
        for ip, count in sorted_ip_counts:
            print(f"{ip}\t\t{count}")                                                          

    except FileNotFoundError:
        print(f"文件 {file_path} 不存在。")                                                          

# 示例用法
file_path = r"学习\FwLog.log"  # 替换为实际的日志文件路径
count_and_sort_ip_in_log(file_path)
