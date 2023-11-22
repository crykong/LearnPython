import requests
import re
import threading

from pyecharts.charts import Pie
from pyecharts import options as opts

country_list = []
gdp_list = []


def get_gdp():
    url = "http://127.0.0.1:8080/gdp.html"
    data = requests.get(url).content.decode("utf-8")
    # print(data)
    data = data.split('\n')
    for row in data:
        # 匹配国家
        result = re.match('.*<a href=""><font>(.*)</font></a>.*', row)
        if result:
            country_list.append(result.group(1))

        result = re.match('.*￥(.*)亿元.*', row)
        if result:
            gdp_list.append(float(result.group(1)))


    data =  list(zip(country_list, gdp_list))

    c = (
        Pie(init_opts=opts.InitOpts(width="1400px", height="600px"))
        .add("", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="2020全球GDP数据"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
        .render("gdp2020.html")
    )
if __name__ == '__main__':
        get_gdp_thread = threading.Thread(target=get_gdp)
        get_gdp_thread.start()
