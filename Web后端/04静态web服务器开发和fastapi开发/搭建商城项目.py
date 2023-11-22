from fastapi import FastAPI
from fastapi import Response

import uvicorn

app = FastAPI()

# 首页
@app.get('/')
def main():
    with open("shopping/index.html", "rb") as f:
        data = f.read()

    return Response(content=data, media_type="text/html")

@app.get("/images/{path}")
def get_pic(path: str):
    with open(f"shopping/images/{path}", "rb") as f:
        data = f.read()
    return Response(content=data, media_type="jpg")

@app.get("/upload/{path}")
def get_upload(path: str):
    with open(f"shopping/upload/{path}", "rb") as f:
        data = f.read()
    return Response(content=data, media_type="png")

# 使用装饰器处理小图标的请求
@app.get("/favicon.ico")  # /images/1.jpg 通过参数进行匹配 正则匹配 路径的后缀
def get_ico():
    with open(f"shopping/favicon.ico", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="image/x-icon")


# 使用装饰器处理css的请求
@app.get("/css/{path}")  # /images/1.jpg 通过参数进行匹配 正则匹配 路径的后缀
def get_css(path:str):
    with open(f"shopping/css/{path}", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="image/x-icon")

# 使用装饰器处理html请求
@app.get("/{path}")  # /images/1.jpg 通过参数进行匹配 正则匹配 路径的后缀
def get_html(path: str):
    with open(f"shopping/{path}", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="text/html")

@app.get("/font/{path}")
def get_fonts(path:str):
    with open(f"shopping/fonts/{path}", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="text/html")

uvicorn.run(app, host='127.0.0.1', port=9090)
