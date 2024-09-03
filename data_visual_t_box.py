import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl
import plotly
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go
import dateparser
import numpy as np

mpl.rcParams["font.family"] = "FangSong"  # 设置字体
mpl.rcParams["axes.unicode_minus"] = False  # 正常显示负号

#导入数据
data = pd.read_excel('F:\shuju\清洗后数据.xlsx',converters = {'社保卡号':str,'商品编码':str})

sales_amount = data.groupby(['销售时间'],as_index = False).mean()

fig = px.box(sales_amount,
              x='销售时间_month',
              y='应收金额',
              points = 'all',
              color = '销售时间_month')

fig.show()