import socket

if __name__ == '__main__':
    while True:
        # 1、创建服务器端套接字对象
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2、绑定IP地址与端口号
        tcp_server_socket.bind(('127.0.0.1', 8000))
        # 3、开启监听
        tcp_server_socket.listen(128)
        # 4、等待接收客户端连接请求（客户端向服务器发送请求通过）
        new_socket, ip_port = tcp_server_socket.accept()
        ip, port = ip_port
        # print(tcp_server_socket)
        # 5、接收数据
        content = new_socket.recv(1024).decode() # decode()默认的编码格式为gbk
        print(f"{ip, port}客户端发送过来的数据；{content}")
        # 6、发送数据
        new_socket.send("信息已经收到,over!".encode("utf-8"))

        # 7、关闭套接字 关闭新套接字对象(不能收发消息)与服务端套接字对象(不能再去接受客户端连接了)
        new_socket.close()
        tcp_server_socket.close()