#!/usr/bin/env python
# -*- coding: utf-8 -*-

#统计LINUX 登录日志出现的IP地址次数
import re                                                                                
def count_and_sort_ip_in_log(file_path):
    try:
        ip_counts = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            content=file.readline()
            # print(content)
            # ip_adress=re.findall('sa', content)
            # print(ip_adress)

            while content:                                                                                                                                
                
                #ip_adress=re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', content)
                ip_adress=re.findall(r'sa=\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', content) #匹配sa=的源IP地址，根据自己需要的写正则表达式
                #ip_adress=re.findall(r'sport=\d{1,5}', content) 

                if ip_adress:                                                                                                                                
                    sa_ip = str(ip_adress[0]) #得到sa=的源IP地址
                    ip=sa_ip[3:] #得到源IP地址,切割数据                                                                                                                                
                    if ip not in ip_counts:
                        ip_counts[ip] = 1                                                                                                                                
                    else:                                                                                                                                
                        ip_counts[ip] += 1                                                                                                                                
                content=file.readline()
        sorted_ip_counts = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
            # for line in file:
            #     ip_adress=re.match(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)
            #     print(ip_adress)
            #     ip = line.split()[0]  # 假设 IP 地址是每行的第一个字段
            #     if ip not in ip_counts:
            #         ip_counts[ip] = 1
            #     else:
            #         ip_counts[ip] += 1

        # 按照出现次数降序排列 IP 地址
        #sorted_ips = sorted(ip_counts.items(), key=lambda item: item[1], reverse=True)

        print(f"IP 地址\t\t出现次数\t 一共出现{len(sorted_ip_counts)}个不同的IP地址")
        print("-----------------------")
        for ip, count in sorted_ip_counts:
            print(f"{ip}\t\t{count}")                                                          

    except FileNotFoundError:
        print(f"文件 {file_path} 不存在。")                                                          

# 示例用法
file_path = r"学习\FwLog.log"  # 替换为实际的日志文件路径
count_and_sort_ip_in_log(file_path)
