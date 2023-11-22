from fastapi import FastAPI
from fastapi import Response

import uvicorn

app = FastAPI()

# 首页
@app.get('/')
def main():
    with open("shopping/index.html", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="text/html")
@app.get("/images/1.jpg")
def func1():
    with open("source/images/1.jpg", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="jpg")

@app.get("/images/2.jpg")
def func2():
    with open("source/images/2.jpg", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="jpg")

@app.get("/images/3.jpg")
def func3():
    with open("source/images/3.jpg", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="jpg")

@app.get("/images/4.jpg")
def func4():
    with open("source/images/4.jpg", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="jpg")


@app.get("/images/5.jpg")
def func5():
    with open("source/images/2.jpg", 'rb') as f:
        data = f.read()

    return Response(content=data, media_type="jpg")

uvicorn.run(app, host='127.0.0.1', port=9091)