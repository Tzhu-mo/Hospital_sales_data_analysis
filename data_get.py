import wget
import os

download_a = "https://gzc-dfsdown.mail.ftn.qq.com/1371/ZF0005_MM7NTEGM60AupGUA~lTe0dc?dkey=5GJXC9MXPk-ftIyMd3ZaGj1jmeLCx2Qb4jSe0YzFwUsKrz6hDS9bcRtrNwkpReLo11eYvSqRRQ_Z8XUgERzHyjw&fname=%E6%9C%9D%E9%98%B3%E5%8C%BB%E9%99%A22018%E5%B9%B4%E9%94%80%E5%94%AE%E6%95%B0%E6%8D%AE.xlsx&eggs"

path = "F:\shuju"

rename = "朝阳医院2018年销售数据.xlsx"

wget.download(download_a, out=os.path.join(path,rename))