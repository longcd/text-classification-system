# encoding:utf-8
# Author:longcd

import jieba
from load_data import load_data


def seg_corpus(cons, seg_filename='./seg_corpus.txt'):
    """使用jieba完成分词，并去停用词

        newsDataSet: list, 每个元素为新闻分词后的内容
    """
    # 载入停用词
    with open('./stopwords.txt', 'rb') as f_stop:
        f_stop_word = f_stop.read().decode('utf-8', 'ignore')

    print('载入停用词完成！')

    with open(seg_filename, 'wb') as fw:
        for i in range(0, len(cons)):
            seg_list = []
            for word in jieba.cut(cons[i], HMM=False):
                if word not in f_stop_word and word != '\ue40c':
                    seg_list.append(word)

            fw.write(' '.join(seg_list).encode('utf-8', 'ignore'))
            fw.write('\n'.encode('utf-8'))
            
    print("分词和去停用词完成！")