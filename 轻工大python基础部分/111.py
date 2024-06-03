#
# @Time   : 2023/12/15 
# @Author : wuBerlin
# @File   : 111.py
import socket


def scan_ip_range(ip_range):
    for ip in ip_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, 20))  # 你可以修改端口号，这里使用80端口
        if result == 0:
            print(f"Port {20} is open on IP {ip}")
        sock.close()

    # 定义IP网段，这里使用125.220.*.*，你可以修改为你需要的网段


ip_range = ['1.220.' + str(i) + '.' + str(j) for i in range(0, 256) for j in range(0, 256)]
scan_ip_range(ip_range)
