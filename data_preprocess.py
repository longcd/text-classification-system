# encoding:utf-8
# Author:longcd

import os
import re
import pickle
import jieba

file_dir = './train' # 数据集目录
labels_name = os.listdir(file_dir) # train目录下每个子目录为一个类别, 如C000007, C000008, C000010

labels = [] # 类标号
cons = [] # 内容

# 加载数据集
def load_data():
    for label in labels_name:
        filenames = os.listdir(os.path.join(file_dir, label))
        data_file = filenames[0:1000] # 每类取1000个

        for fn in data_file:
            with open(os.path.join(file_dir, label, fn), 'rb') as f:
                file_content = f.read()
            uniStr = file_content.decode('gb18030', 'ignore')
            labels.append(label)
            cons.append(uniStr)
    return cons, labels
    
    
def seg_corpus(cons, seg_filename='./seg_corpus.txt'):
    """使用jieba完成分词，并去停用词
    """
    # 载入停用词
    with open('./stopwords.txt', 'rb') as f_stop:
        f_stop_word = f_stop.read().decode('utf-8', 'ignore')
    print('载入停用词完成！')

    with open(seg_filename, 'wb') as fw:
        for i in range(0, len(cons)):
            seg_list = []
            for word in jieba.cut(cons[i], HMM=False): # 使用jieba分词进行文本分词
                if (word not in f_stop_word) and (len(word) != 1) and (word != '\r\n'):
                    pattern = re.compile(r'\d')
                    match = pattern.match(word)
                    if not match:
                        seg_list.append(word)

            fw.write(' '.join(seg_list).encode('utf-8', 'ignore')) # 每个词以空格分开
            fw.write('\n'.encode('utf-8')) # 一行一篇新闻


cons, labels = load_data()
seg_corpus(cons, seg_filename='./seg_corpus.txt')

with open('./labels.pickle','wb') as f:  
    #dump()函数接受一个可序列化的Python数据结构  
    pickle.dump(labels,f)  
    print('success')

        
