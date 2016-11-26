# 文本分类

文本分类，使用搜狗文本分类语料库

## 1.主要步骤

- 文本分词处理
- 特征选择
- 特征权重计算
- 文本特征向量表示
- 训练模型并测试：kNN、NB、SVM
- 使用爬虫抓取新闻并测试

## 2.数据集

### 英文文本

数据集使用著名的[`20 Newsgrousps`](http://www.qwone.com/~jason/20Newsgroups/)新闻数据集，你可以从[这里](http://www.qwone.com/~jason/20Newsgroups/20news-bydate.tar.gz)下载。

数据加载使用[`sklearn.datasets.load_files`](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_files.html)来加载数据集。

### 中文文本

使用[`搜狐新闻数据(SogouCS)`](http://www.sogou.com/labs/resource/cs.php)的精简版数据其中的一部分。

## 3.运行环境

- python 3.4
- scikit-learn
- numpy
- jieba

## 4.示例

### 运行HTTP服务器

![image](https://github.com/longcd/Text-Classification-System/raw/master/test0.png)

### 打开页面

![image](https://github.com/longcd/Text-Classification-System/raw/master/test1.png)

### 今日头条上的新闻

![image](https://github.com/longcd/Text-Classification-System/raw/master/test2.png)

### 测试结果

![image](https://github.com/longcd/Text-Classification-System/raw/master/test3.png)