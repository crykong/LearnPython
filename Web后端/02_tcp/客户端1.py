# ① 导入socket模块
import socket

# 创建socket对象
"""
操作参数名说明
AF_INET IPv4
AddressFamily IP地址类型, 分为IPv4和IPv6 
Type 传输协议类型 SOCK_STREAM tcp协议

"""
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 和服务器端套接字建立连接(参数必须是一个元祖)
tcp_client_socket.connect(("127.0.0.1", 9090))
tcp_client_socket.send("你好, 服务器,我是tcp客户端".encode(encoding="gbk"))

# 接受数据
server_data = tcp_client_socket.recv(1024).decode(encoding="gbk")
print(server_data)

# 关闭连接
tcp_client_socket.close()