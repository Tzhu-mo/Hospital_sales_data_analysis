import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error, mean_absolute_error

data = pd.read_excel(r'F:\shuju\训练数据.xlsx')
data.fillna(method='ffill', inplace=True)

data['销售时间'] = data.销售时间.map(lambda x: x.strftime('%Y%m%d'))
data['商品编码'] = data['商品编码'].astype(str)

x = data[['销售时间', '商品编码']]
y = data['销售数量']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

clf = KNeighborsClassifier(n_neighbors=3)

# 使用训练集进行模型训练
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

test_accuracy = r2_score(y_test, y_pred)

print("测试集准确率:", test_accuracy)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# 输出结果
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"R-squared (R²): {r2:.4f}")

plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--k')
plt.xlabel('True values')
plt.ylabel('Predictions')
plt.title('K-Nearest Neighbors')
plt.show()