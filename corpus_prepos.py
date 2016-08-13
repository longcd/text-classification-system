# -*- encoding: utf-8 -*-

import os

# 分类语料库路径
corpus_path = "tc-corpus-answer/answer/"
# 预测理后分类语料库路径
pos_path = "text_corpus_pos/"

# 获取corpus_path下的所有子目录,目录名为语料库的分类
class_list = os.listdir(corpus_path)

# 获取并处理每个子目录下所有的文件
for mydir in class_list:
    class_path = corpus_path + mydir + "/" # 分类子目录的全路径
    file_list = os.listdir(class_path) # 获取分类子目录下的所有文件
    for file_name in file_list:
        file_path = class_path + file_name # 文件名全路径
        try:
            with open(file_path, 'r', encoding='gb18030') as file:
                raw_corpus = file.read() # 读取未处理的预料
                corpus_list = raw_corpus.splitlines() # 按行切分字符串为一个列表
                raw_corpus = ""
                for line in corpus_list:
                    line = line.strip()
                    if line.find('【 文献号 】') != -1:
                        line = ""
                    elif line.find('【原文出处】') != -1:
                        line = ""
                    elif line.find('【原刊地名】') != -1:
                        line = ""
                    elif line.find('【原刊期号】') != -1:
                        line = ""
                    elif line.find('【原刊页号】') != -1:
                        line = ""
                    elif line.find('【分 类 号】') != -1:
                        line = ""
                    elif line.find('【分 类 名】') != -1:
                        line = ""
                    elif line.find('【 作  者 】') != -1:
                        line = ""
                    elif line.find('【复印期号】') != -1:
                        line = ""
                    elif line.find('【 正  文 】') != -1:
                        line = ""
                    if line != "":
                        raw_corpus += line

                # 分词后语料分类目录
                pos_dir = pos_path + mydir + "/"
                if not os.path.exists(pos_dir):
                    os.makedirs(pos_dir)
                    
                with open(pos_dir + file_name, 'w', encoding='gb18030') as fw:
                    fw.write(raw_corpus)

        # 有些文件存在UnicodeDecodeError，这里简单地忽略掉
        except UnicodeDecodeError:
            print('UnicodeDecodeError:' + file_name)
            continue


print("语料预处理完成！")