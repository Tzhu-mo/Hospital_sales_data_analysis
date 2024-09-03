from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_excel('F:\shuju\训练数据.xlsx')
data.fillna(method='ffill', inplace=True)

data['销售时间'] = data.销售时间.map(lambda x: x.strftime('%Y%m%d'))
data['商品编码'] = data['商品编码'].astype(str)

x = data[['销售时间','商品编码']]
y = data['销售数量']

x_train,x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = linear_model.LinearRegression()  # 创建一个模型对象
model.fit(x_train, y_train)  # 将x和y分别作为自变量和因变量输入模型进行训练

y_pred_model = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred_model)
r2 = r2_score(y_test, y_pred_model)

print("均方误差：", mse)
print("R2 分数：", r2)
print('各系数'+str(model.coef_))
print('各常数项'+str(model.intercept_))

plt.scatter(y_test, y_pred_model, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--k')
plt.xlabel('True values')
plt.ylabel('Predictions')
plt.title('Linear Regression')
plt.show()