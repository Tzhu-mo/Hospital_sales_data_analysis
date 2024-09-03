import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib as mpl
import warnings
warnings.filterwarnings('ignore')

mpl.rcParams["font.family"] = "FangSong"  # 设置字体
mpl.rcParams["axes.unicode_minus"] = False  # 正常显示负号

data = pd.read_excel(r'F:\shuju\训练数据.xlsx')
data.fillna(method='ffill', inplace=True)

data_1 = data[data['销售时间'].dt.month.isin(np.arange(1,7))]
data_2 = data[data['销售时间'].dt.month.isin(np.arange(7,8))]

data_1['销售时间'] = data_1.销售时间.map(lambda x: x.strftime('%Y%m%d'))
data_1['商品编码'] = data_1['商品编码'].astype(str)

data_2['销售时间'] = data_2.销售时间.map(lambda x: x.strftime('%Y%m%d'))
data_2['商品编码'] = data_2['商品编码'].astype(str)

x = data_1[['销售时间', '商品编码']]
y = data_1['销售数量']

#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

clf = KNeighborsClassifier(n_neighbors=3)

# 使用训练集进行模型训练
clf.fit(x, y)

#预测七月份数据
x_2 = data_2[['销售时间', '商品编码']]
y_2 = data_2['销售数量']
y_2_pred = clf.predict(x_2)

data_pre = x_2
data_pre['销售数量_真实值'] = y_2
data_pre['销售数量_预测值'] = y_2_pred

data_pred_tj = data_pre.groupby('商品编码').agg({'销售数量_真实值':sum,'销售数量_预测值':sum})


plt.title('七月份销售数量真实值与预测值对比')  # 折线图标题

plt.xlabel('商品编码')  # x轴标题
#plt.ylabel('差值')  # y轴标题
plt.plot(data_pred_tj.index, data_pred_tj.销售数量_真实值)  # 绘制折线图，添加数据点，设置点的大小
plt.plot(data_pred_tj.index, data_pred_tj.销售数量_预测值)

plt.legend(['销售数量_真实值', '销售数量_预测值'], loc='upper right')  # 设置折线名称
plt.xticks(rotation=270)
plt.savefig(r'E:\my_python_projects\table\predictions_七月.png')
#8月份各种药品的销售数量预测折线图
'''
plt.figure()
x = data_pred_tj.index
y = data_pred_tj.销售数量
plt.plot(x,y)
plt.title('七月份销售数量折线图')
plt.xlabel('商品编码')
plt.ylabel('销售数量')
plt.xticks(rotation=270)
plt.savefig(r'E:\my_python_projects\table\predictions_八月.png')
'''
plt.show()