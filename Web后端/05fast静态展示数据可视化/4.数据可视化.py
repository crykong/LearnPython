# 选择图形 饼图
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.faker import Faker

c = (
    Pie(init_opts=opts.InitOpts(width='1600px', height="1000px"))
    .add("", [list(z) for z in zip(Faker.fruits, Faker.values())])
    .set_global_opts(title_opts=opts.TitleOpts(title="水果销售量"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
    .render("pie_base.html")
)