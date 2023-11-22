# 导入FastAPI模块
from fastapi import FastAPI
# 导入响应报文Response模块
from fastapi import Response
# 导入服务器uvicorn模块
import uvicorn

# 创建FastAPI框架对象
app = FastAPI()


# 通过@app路由装饰器收发数据
# @app.get(参数) : 按照get方式接受请求数据
# 请求资源的 url 路径
# \/
# 静态资源 static
@app.get("/{path}")
def main(path:str):
    with open(f"source/html/{path}", "rb") as f:
        data = f.read()
    # return 返回响应数据
    # Response(content=data, media_type="text/html"
    # 参数1: 响应数据
    # 参数2: 数据格式
    return Response(content=data, media_type="text/html")

# 当浏览器发出对图片 0.jpg 的请求时, 函数返回相应资源
@app.get("/images/{path}")
def func_01(path:str):
    with open(f"source/images/{path}", "rb") as f:
        data = f.read()
        # print(data)
    return Response(content=data, media_type="jpg")

# 运行服务器
# 参数1: 框架对象
# 参数2: IP地址
# 参数3: 端口号
uvicorn.run(app, host="127.0.0.1", port=8080)