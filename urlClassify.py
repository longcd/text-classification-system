# -*- coding: utf-8 -*-

import re
import jieba
import pickle
from urllib.request import urlopen
from bs4 import BeautifulSoup


# 使用BeautifulSoup, 获取新闻的内容
def getArticle(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), 'lxml')
    article_content = bsObj.select('div.article-content')
    return article_content[0].get_text()


# 使用jieba分词, 对新闻进行分词, 并去停用词
def seg_corpus(article_cons):
    """使用jieba完成分词，并去停用词
    """
    # 载入停用词
    with open('./stopwords.txt', 'rb') as f_stop:
        f_stop_word = f_stop.read().decode('utf-8', 'ignore')
    print('载入停用词完成！')


    word_seg_list = []
    for word in jieba.cut(article_cons, HMM=False): # 使用jieba分词进行文本分词
        if (word not in f_stop_word) and (len(word) != 1) and (word != '\r\n'): # 去停用词
            pattern = re.compile(r'\d')
            match = pattern.match(word)
            if not match:
                word_seg_list.append(word)

    seg_str = ' '.join(word_seg_list).encode('utf-8', 'ignore')
    segment = []
    segment.append(seg_str)
    return segment

# 进行文本分类预测
def predict(segment):
    data = {}
    with open('./text_classify.pickle', 'rb') as f:
        data = pickle.load(f)

    test_corpus_counts = data['count_vect'].transform(segment)
    test_corpus_tfidf = data['tfidf_transformer'].transform(test_corpus_counts)
    pred = data['mnbclf'].predict(test_corpus_tfidf)
    return pred