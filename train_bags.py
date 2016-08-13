# -*- encoding: utf-8 -*-

import os
import pickle
from sklearn.datasets.base import Bunch

# 分词后分类语料库路径
seg_path = "text_corpus_segment/"

# 词袋语料路径
wordbag_path = "text_corpus_wordbag/"
if not os.path.exists(wordbag_path):
    os.makedirs(wordbag_path)

# Bunch类提供一种key,value的对象形式
# target_name:所有分类名称列表
# label:每个文件的分类标签列表
# filenames:文件名称
# contents:文件内容
data_set = Bunch(target_name=[], label=[], filenames=[], contents=[])

# 获取seg_path下的所有子分类
class_list = os.listdir(seg_path)
data_set.target_name = class_list

# 获取每个子目录下所有的文件
for mydir in class_list:
  class_path = seg_path + mydir + "/"
  file_list = os.listdir(class_path) # 获取class_path下的所有文件
  for file_name in file_list:
      file_path = class_path + file_name
      data_set.filenames.append(file_path) # 把文件路径附加到数据集中
      data_set.label.append(data_set.target_name.index(mydir)) # 把文件分类标签附加到数据集中
      with open(file_path, 'r', encoding='gb18030') as file:
          seg_corpus = file.read() # 读取语料
          data_set.contents.append(seg_corpus) # 构建分词文本内容列表


# 训练集对象持久化
with open(wordbag_path + 'train_set.data', 'wb') as file_obj:
    pickle.dump(data_set, file_obj)


# 验证结果
with open(wordbag_path + 'train_set.data', 'rb') as file_obj:
    data_set = {} # 清空原有数据集
    data_set = pickle.load(file_obj)
    # 输出数据集包含的所有类别
    print(data_set.target_name)
    # 输出数据集包含的所有类别标签树
    print(len(data_set.label))
    # 输出数据集包含的文件数
    print(len(data_set.contents))
