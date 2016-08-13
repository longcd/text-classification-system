# -*- encoding: utf-8 -*-

import os
import jieba

# 预处理后分类语料库路径
corpus_path = "text_corpus_pos/"

# 分词后分类语料库路径
seg_path = "text_corpus_segment/"

# 获取corpus_path下的所有子目录
class_list = os.listdir(corpus_path)

# 获取每个目录下所有的文件
for mydir in class_list:
    class_path = corpus_path + mydir + "/" # 分类子目录的全路径
    file_list = os.listdir(class_path)
    for file_name in file_list:
        file_path = class_path + file_name # 文件名全路径
        with open(file_path, 'r', encoding='gb18030') as file:
            raw_corpus = file.read() # 读取未分词语料
            seg_corpus = jieba.cut(raw_corpus) # 结巴分词操作

            # 分词后语料分类目录
            seg_dir = seg_path + mydir + "/"
            if not os.path.exists(seg_dir):
                os.makedirs(seg_dir)

            with open(seg_dir + file_name, 'w', encoding='gb18030') as fw:
                fw.write(" ".join(seg_corpus)) # 用空格将分词结果分开并写入分词后语料文件中


print("语料分词完成！")