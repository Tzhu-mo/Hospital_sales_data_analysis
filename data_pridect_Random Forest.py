from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


data = pd.read_excel(r'F:\shuju\训练数据.xlsx')
data.fillna(method='ffill', inplace=True)

data['销售时间'] = data.销售时间.map(lambda x: x.strftime('%Y%m%d'))
data['商品编码'] = data['商品编码'].astype(str)

x = data[['销售时间', '商品编码']]
y = data['销售数量']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
test_accuracy = accuracy_score(y_test, y_pred)
print("测试集准确率:", test_accuracy)

plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--k')
plt.xlabel('True values')
plt.ylabel('Predictions')
plt.title('Random Forest')
plt.show()