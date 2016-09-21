# 使用scikit-learn进行文本分类

本项目的目标是使用scikit-learn进行文本分类。

项目使用 `jupyter notebook (ipython notebook)` 进行展示。

`Github` 加载 `.ipynb` 的速度较慢，建议在 [Nbviewer](http://nbviewer.jupyter.org/github/longcd/Text-Classification-System/blob/master/text_classification.ipynb) 中查看该项目。

----

本项目将运用到以下知识：

- TF-IDF
- 朴素贝叶斯
- 最近邻
- 支持向量机
- 参数调优
- 验证
- 评价


## 数据集

数据集使用著名的[`20 Newsgrousps`](http://www.qwone.com/~jason/20Newsgroups/)新闻数据集，你可以从[这里](http://www.qwone.com/~jason/20Newsgroups/20news-bydate.tar.gz)下载。

数据加载使用[`sklearn.datasets.load_files`](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_files.html)来加载数据集。

## 运行环境

- python 3.4
- scikit-learn
- numpy

## 实验过程

### Experiment 1: NB

在这个实验中,将文本转成Tf-Idf矩阵，同时使用贝叶斯分类器进行训练及测试。

测试使用数据集中的`test`子集。

Results:
```
training time: 8.613000
testing time: 2.350000
Accuracy: 0.816914498141
```

### Experiment 2: SVM

使用支持向量机分类器进行训练及测试。

Results:
```
training time: 154.876000
testing time: 58.943000
Accuracy: 0.83497079129
```

### Experiment 3: kNN

使用k最近邻分类器进行训练及测试。

Results:
```
training time: 3.943000
testing time: 28.372000
Accuracy: 0.675783324482
```

### Experiment 4: 优化后的SVM

使用支持向量机分类器进行训练及测试。。

Results:
```
Accuracy:  0.837095061073

```

## 总结

文本预处理过程包含的步骤总结如下：

- 切分文本（分词）
- 删除出现过于频繁，而又对匹配相关文档没有帮助的词语（去停用词）
- 删除出现频率很低，只有很小可能出现在未来帖子中的词语
- 统计剩余的词语
- 考虑整个预料集合，从词频统计中计算TF-IDF值

通过这一过程，我们将一堆充满噪声的文本转换成了一个简明的特征表示。然而，虽然词袋模型及其扩展简单有效，但仍然有一些缺点需要注意：

- 它并不涵盖词语之间的关联关系。采用之前的向量化方法，文本”Car hits wall”和”Wall hits car”会有相同的特征向量。
- 它没法捕捉否定关系。例如”I will eat ice cream”和”I will not eat ice cream”，尽管它们意思截然相反，但从特征向量来看它们非常相似。这个问题其实很容易解决，只需要既统计单个词语（又叫unigrams），又考虑成队的词语（bigrams）或者trigrams（一行中的三个词语）即可。
- 对于拼写错误的词语会处理失败。
