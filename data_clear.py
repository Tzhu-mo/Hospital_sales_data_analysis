import pandas as pd

#导入数据
data = pd.read_excel('F:\shuju\朝阳医院2018年销售数据.xlsx',converters = {'社保卡号':str,'商品编码':str})

#购药时间改为销售时间
nameChangeDict = {"购药时间":"销售时间"}
data.rename(columns = nameChangeDict,inplace=True)

#首先查看一下哪些项目存在缺失值
print('是否存在缺失值：')
print(data.isnull().any())
#查看一下缺失值的数量
#通常可以用isnull函数来查找缺失值
print(data[data[['销售时间','社保卡号']].isnull().values == True])

#去掉重复数据。
naDf = data[data[['销售时间','社保卡号']].isnull().values == True].drop_duplicates()

#去掉缺失数据
data = data.dropna(subset=['销售时间','社保卡号'],how = 'any')

#重命名行名（index）：排序后的列索引值是之前的行号，需要修改成从0到N按顺序的索引值
data=data.reset_index(drop=True)

#转换数据类型
data['销售数量'] = data['销售数量'].astype('float')
data['应收金额'] = data['应收金额'].astype('float')
data['实收金额'] = data['实收金额'].astype('float')
print('转换后的数据类型：\n',data.dtypes)

#日期转换，取出年月日
def dateChange_date(dateSer):
    dateList = []
    for i in dateSer:
        #例如2018-01-01 星期五，分割后为：2018-01-01
        str = i.split(' ')[0]
        dateList.append(str)
    dateChangeSer = pd.Series(dateList)
    return dateChangeSer
dateChangeSer = dateChange_date(data['销售时间'])
dateChangeSer.head(5)

#取出星期
def dateChange_day(dateSer):
    dateList = []
    for i in dateSer:
        str = i.split(' ')[1]
        dateList.append(str)
    dateChangeSer = pd.Series(dateList)
    return dateChangeSer
dateChangeSer_day = dateChange_day(data['销售时间'])
dateChangeSer_day.head(5)

data['销售时间'] = dateChangeSer
data['星期'] = dateChangeSer_day

#查看是否有缺失值
print('是否有缺失值')
print(data['销售时间'].isnull().any())

#转换销售时间为日期型
dateSer=pd.to_datetime(data['销售时间'], format = '%Y-%m-%d', errors='coerce')

compareDf = pd.DataFrame(dateSer[dateSer.isnull()],data[dateSer.isnull()]['销售时间'])

#去除错误值
data['销售时间'] = dateSer

data=data.dropna(subset=['销售时间','社保卡号'],how='any')

data=data.reset_index(drop=True)

#按销售时间排序
data = data.sort_values(by='销售时间')
#再次更新一下序号
data = data.reset_index(drop = True)

#删除异常值：通过条件判断筛选出数据
#查询条件
querySer=data.loc[:,'销售数量']>0
#应用查询条件
print('删除异常值前：',data.shape)
data=data.loc[querySer,:]
print('删除异常值后：',data.shape)

#添加销售月份的列
data["销售时间_month"] = data["销售时间"].apply(lambda x:x.month)

print(data.head(20))

data.to_excel('F:\shuju\清洗后数据.xlsx')

#训练模型使用的数据
data_1 = data.groupby(['销售时间','商品编码'],as_index = False).agg({'销售数量':sum,'应收金额':sum})
data_1.to_excel('F:\shuju\训练数据.xlsx')