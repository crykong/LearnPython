import requests
import re

def get_pic_url():
    response = requests.get('http://127.0.0.1:8090/index.html')
    res = response.content.decode("utf-8")
    data = res.split("\n")
    # print(data)
    # 创建一个列表存储所有图片的url地址(也就是图片网址)
    url_list = []
    for i in data:
        result = re.match('.*src="(.*)" width', i)
        if result: # 字符串  有内容 if 进行判断正确 true  None = 0 = false
            url_list.append(result.group(1))
    return url_list
# 保存图片
def save_pic(pic_url_list):
    num = 0
    for pic_url in  pic_url_list:
        print("http://127.0.0.1:8000" + pic_url[1:])
        res = requests.get("http://127.0.0.1:8090" + pic_url[1:])
        with open(f"source/spyder/{num}.jpg", "wb") as f:
            f.write(res.content)
        num += 1

if __name__ == '__main__':
    pic_url_list = get_pic_url()
    save_pic(pic_url_list)