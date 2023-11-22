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

        # 获取用户请求的资源页面
        request_data = client_request_data.split(' ', maxsplit=2)
        request_path = request_data[1] # '/list.html'

        # 解决域名是否直接访问首页的问题
        if request_path == '/': # 代表用户直接访问首页
            request_path = '/index.html'


        # 返回数据给浏览器端
        try:
            with open("html" + request_path, "rb") as f:
                file_data = f.read()
        except Exception as ex:
        # 处理以上文件不存在,则返回404，返回错误信息
            response_line = 'HTTP/1.1 404 Not Found\r\n'
            response_header = 'Server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
            response_body = '<h1>非常抱歉，您当前访问的网页已经不存在了</h1>'.encode('utf-8')
            response_data = (response_line + response_header + '\r\n').encode('utf-8') + response_body
            print(response_data, ex)
        else:
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
        finally:

            # 6、关闭客户端socket连接
            client_socket.close()