import socket

"""
监听：设置监听 => 设置允许最大的监听数 => 128
等待接收客户端连接请求(关键点、难点)
accept()方法：接受客户端连接，accept方法在接受的同时，如何识别到底是哪个客户端发起的连接呢？
"""

if __name__ == '__main__':
    # 1、创建服务器端套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、绑定IP地址与端口号
    tcp_server_socket.bind(('127.0.0.1', 8000))
    # 3、开启监听
    tcp_server_socket.listen(128)
    # 4、等待接收客户端连接请求
    new_socket, ip_port = tcp_server_socket.accept()
    # print(tcp_server_socket)

    print(new_socket) # 新问题: 新套接字对象到底用来做什么？
    print(ip_port) # 客户端的IP + 端口
    # 5、接收数据
    # 6、发送数据
    # 7、关闭套接字

"""
<socket.socket fd=340, family=2, type=1, proto=0, laddr=('127.0.0.1', 8000)>
<socket.socket fd=376, family=AF_INET, type=SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 57222)>

socket.socket(socket.AF_INET, socket.SOCK_STREAM)
本质上是一个元组， 元组内部可以存放多个元素，元素和元素之间通过逗号隔开
第一个参数是一个socket套接字对象 
第二个参数也是一个元组，元组有两个值(ip地址+端口号)，通过查看内容可知，这里代表客户端的Ip+端口
('127.0.0.1', 57222)
"""