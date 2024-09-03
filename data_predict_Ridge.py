from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_excel(r'F:\shuju\训练数据.xlsx')
data.fillna(method='ffill', inplace=True)

data['销售时间'] = data.销售时间.map(lambda x: x.strftime('%Y%m%d'))
data['商品编码'] = data['商品编码'].astype(str)

x = data[['销售时间', '商品编码']]
y = data['销售数量']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

rr = linear_model.Ridge(alpha=0.0001)
rr.fit(x_train, y_train)
y_pre_rr = rr.predict(x_test)
mse2 = mean_squared_error(y_test, y_pre_rr)

print('Ridge(数据未标准化)：')
print("均方误差：", mse2)
print('各系数'+str(rr.coef_))
print('各常数项'+str(rr.intercept_))
print()

plt.scatter(y_test, y_pre_rr, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--k')
plt.xlabel('True values')
plt.ylabel('Predictions')
plt.title('Ridge')
plt.show()