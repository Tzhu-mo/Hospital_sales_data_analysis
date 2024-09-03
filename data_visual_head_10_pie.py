import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"C:\Windows\Fonts\Simkai.ttf", size=14)

mpl.rcParams["font.family"] = "FangSong"  # 设置字体
mpl.rcParams["axes.unicode_minus"] = False  # 正常显示负号

data = pd.read_excel('F:\shuju\清洗后数据.xlsx',converters = {'社保卡号':str,'商品编码':str})
print(data.head())
#统计每种商品['销售数量','应收金额','实收金额']
sales_volume = pd.pivot_table(data,index = ['商品名称'],values = ['销售数量','应收金额','实收金额'],aggfunc='sum',fill_value = 0)

#销售量前十的药品饼图
sales_volume_sorted_mo = sales_volume.sort_values(by='应收金额',ascending = False)

test = sales_volume_sorted_mo.head(10)

plt.pie(list(test.应收金额), labels=list(test.index), autopct='%1.1f%%')
plt.legend(loc="best", prop=font)
plt.axis('equal')
plt.savefig(r'E:\my_python_projects\table\visual_head_10.png')

plt.show()