from fastapi import FastAPI
from fastapi import Response

import uvicorn

app = FastAPI()


# 首页
@app.get('/')
def main():
    with open("html/index.html", 'rb') as f:
        data = f.read()
    return Response(content=data, media_type="text/html")


# 使用装饰器处理图片请求
@app.get("/images/{path}")  # /images/1.jpg 通过参数进行匹配 正则匹配 路径的后缀
def get_pic(path: str):
    with open(f"source/images/{path}", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="jpg")

# 使用装饰器处理html请求
@app.get("/html/{path}")  # /images/1.jpg 通过参数进行匹配 正则匹配 路径的后缀
def get_html(path: str):
    with open(f"html/{path}", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="text/html")


# 使用装饰器处理小图标的请求
@app.get("/favicon.ico")  # /images/1.jpg 通过参数进行匹配 正则匹配 路径的后缀
def get_ico():
    with open(f"source/html/favicon.ico", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="image/x-icon")

uvicorn.run(app, host='127.0.0.1', port=9092)
