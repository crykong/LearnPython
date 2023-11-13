import socket
import threading

class WebServer(object):
    def __init__(self):
        # 1、创建服务器端套接字对象
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 端口复用，设置端口号服用，让程序退出之后端口号立即释放
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 2、绑定IP地址与端口号
        self.tcp_server_socket.bind(("", 8888))
        # 3、开启监听
        self.tcp_server_socket.listen(128)


        # 定义一个方法start()方法 ==> 接受客户端连接
    def start(self):
        # 4、等待接收客户端连接请求
        while True:
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 5、接收数据
            content = new_socket.recv(1024).decode() # decode()默认的编码格式为gbk
            print(f"{ip_port}客户端发送过来的数据；{content}")
            # 6、发送数据
            data = input("请输入你要回复的内容：")
            new_socket.send(data.encode("utf-8"))
            # 7、关闭套接字 关闭新套接字对象(不能收发消息)与服务端套接字对象(不能再去接受客户端连接了)
            new_socket.close()


ws = WebServer()
ws.star_thread()