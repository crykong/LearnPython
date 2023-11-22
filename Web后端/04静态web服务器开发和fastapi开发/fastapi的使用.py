# 导入FastAPI模块 pip install fastapi
from fastapi import FastAPI
# 导入响应报文Response模块
from fastapi import Response
# 导入服务器uvicorn模块 pip install uvicorn
import uvicorn

# 创建FastAPI框架对象
# 应用程序
app = FastAPI()

# 路由 ！= 路由器
# 路由(Route): 在web开发中，路由指的是将HTTP请求映射相应的处理函数或处理逻辑机制
# 通过@app路由装饰器收发数据
# @app.get(参数) : 按照get方式接受请求数据
# 请求资源的 url 路径
@app.get("/index.html")
def main():
    with open("html/index.html") as f:
        data = f.read()
    # return 返回响应数据
    # Response(content=data, media_type="text/html"
    # 参数1: 响应数据
    # 参数2: 数据格式
    # content就是响应体  media_type=指定HTTP响应的内容类型  用于指示浏览器应当把响应解释为HTML内容
    return Response(content=data, media_type="text/html")


# 运行服务器
# 参数1: 框架对象
# 参数2: IP地址
# 参数3: 端口号
uvicorn.run(app, host="127.0.0.1", port=9093)