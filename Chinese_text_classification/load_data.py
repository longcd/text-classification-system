# encoding:utf-8
# Author:longcd

from bs4 import BeautifulSoup


def getLabel(url):
    """获取新闻的类标号"""

    # 每篇新闻的链接如下：
    # 汽车：
    # http://auto.sohu.com/
    return url.split('/')[2].split('.')[0]


def getArticle(filename):
    """读取文件，并解析URL、content，来获取新闻的类标号及新闻的内容

        labels: list, 每个元素为对应的类标号
        cons: list, 每个元素为新闻的具体内容
    """
    with open(filename, 'rb') as f:
        file_content = f.read()

    # 数据集中的文件为gbk编码，需将其转换为utf-8编码
    uniStr = file_content.decode('gb18030', 'ignore')

    # 数据格式为
    # <doc>
    # <url>页面URL</url>
    # <docno>页面ID</docno>
    # <contenttitle>页面标题</contenttitle>
    # <content>页面内容</content>
    # </doc>
    labels = []
    cons = []

    # 使用BeautifulSoup来解析URL和contents标签里的具体内容
    soup = BeautifulSoup(uniStr, "lxml", from_encoding='utf-8')
    urls = soup.find_all('url')
    contents = soup.find_all('content')

    for url, content in zip(urls, contents):
        # 忽略内容为空的新闻
        if content.get_text() == '':
            continue
        else:
            label = getLabel(url.get_text())
            if label == '2008': # 把奥运会统称为运动
                label = 'sports'
            labels.append(label)
            cons.append(content.get_text())

    return labels, cons


def load_data(filename):
    """载入数据集

        labels: list, 每个元素为对应的类标号
        cons: list, 每个元素为新闻的具体内容
    """
    labels = []
    cons = []

    for fn in filename:
        label, con = getArticle(fn)
        labels.extend(label)
        cons.extend(con)

    print("载入数据完成！")

    return labels, cons


# # testing
# filename = ['./SogouCS.reduced/news.sohunews.010806.txt', 
#             './SogouCS.reduced/news.sohunews.020806.txt',
#             './SogouCS.reduced/news.sohunews.030806.txt']

# labels, cons = load_data(filename)
# print(len(labels))
# print(labels[:5])
# print(len(cons))
# print(cons[:5])