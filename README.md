# 使用scikit-learn进行文本分类

本项目的目标是使用scikit-learn进行文本分类。

项目使用 `jupyter notebook (ipython notebook)` 进行展示。

`Github` 加载 `.ipynb` 的速度较慢，建议在 [**英文文本分类**](http://nbviewer.jupyter.org/github/longcd/Text-Classification-System/blob/master/text_classification.ipynb) 和 [**中文文本分类**](http://nbviewer.jupyter.org/github/longcd/Text-Classification-System/blob/master/Chinese_text_classification/Chinese_text_classification.ipynb) 中查看该项目。

----

本项目将运用到以下知识：

- 分词
- 文本向量化表示
- 朴素贝叶斯
- k最近邻
- 参数调优
- 分类器性能评价

## 数据集

### 英文文本

数据集使用著名的[`20 Newsgrousps`](http://www.qwone.com/~jason/20Newsgroups/)新闻数据集，你可以从[这里](http://www.qwone.com/~jason/20Newsgroups/20news-bydate.tar.gz)下载。

数据加载使用[`sklearn.datasets.load_files`](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_files.html)来加载数据集。

### 中文文本

使用[`搜狐新闻数据(SogouCS)`](http://www.sogou.com/labs/resource/cs.php)的精简版数据其中的一部分。

## 运行环境

- python 3.4
- scikit-learn
- numpy
- jieba

## 总结

文本预处理过程包含的步骤总结如下：

- 切分文本（分词）
- 删除出现过于频繁，而又对匹配相关文档没有帮助的词语（去停用词）
- 删除出现频率很低，只有很小可能出现在文本中的词语（DF）
- 考虑整个预料集合，从词频统计中计算TF-IDF值（向量化表示）

通过这一过程，我们将一堆充满噪声的文本转换成了一个简明的特征表示。然而，虽然词袋模型及其扩展简单有效，但仍然有一些缺点需要注意：

- 它并不涵盖词语之间的关联关系。比如文本”Car hits wall”和”Wall hits car”会有相同的特征向量。
- 它没法捕捉否定关系。例如”I will eat ice cream”和”I will not eat ice cream”，尽管它们意思截然相反，但从特征向量来看它们非常相似。
- 对于书写错误的词语会处理失败。