import socket


if __name__ == '__main__':
    # 1、创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 2、绑定IP和端口
    tcp_server_socket.bind(("", 8080))
    # 3、设置监听
    tcp_server_socket.listen(128)

    while True:
        # 4、建立连接
        client_socket, client_addr = tcp_server_socket.accept()
        client_request_data = client_socket.recv(1024).decode()
        print(client_request_data)

        with open("html/index.html", "rb") as f:
            file_data = f.read()

        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 响应头
        response_header = "Server:pwb\r\n"
        # 响应体
        response_body = file_data

        # 响应数据
        response_data = (response_line + response_header + "\r\n").encode() + response_body

        # 5、发送数据
        client_socket.send(response_data)
        # 6、关闭客户端socket连接
        client_socket.close()