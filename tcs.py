import os
import jieba

def readfile(path):
    with open(path, 'r') as myfile:
        content = ""
        for line in myfile.readlines():
            content += line.strip()
        return content

def savefile(savepath, content):
    with open(savepath, 'w') as myfile:
        myfile.write(content)

corpus_path = "train_corpus_small/"
seg_path = "train_corpus_seg/"

# corpus_path = 'tc-corpus-answer/answer/'
# seg_path = "tc-corpus-answer_seg/"

# catelist = os.listdir(corpus_path)

# for mydir in catelist:
#     class_path = corpus_path + mydir + "/"
#     seg_dir = seg_path + mydir + "/"
#     if not os.path.exists(seg_dir):
#         os.makedirs(seg_dir)
#     file_list = os.listdir(class_path)
#     for file_path in file_list:
#         fullname = class_path + file_path
#         try:
#             content = readfile(fullname)
#             content_seg = jieba.cut(content)
#             savefile(seg_dir + file_path, " ".join(content_seg))
#         except UnicodeDecodeError:
#             print('UnicodeDecodeError:' + fullname)
#             continue


# print("end")

from sklearn.datasets.base import Bunch
import pickle
bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
wordbag_paht = 'train_word_bag/train_set.dat'
seg_path = 'train_corpus_seg/'

catelist = os.listdir(seg_path)
bunch.target_name.extend(catelist)
for mydir in catelist:
    class_path = seg_path + mydir + '/'
    file_list = os.listdir(class_path)
    for file_path in file_list:
        fullname = class_path + file_path
        bunch.label.append(mydir)
        bunch.filenames.append(fullname)
        bunch.contents.append(readfile(fullname).strip())

file_obj = open(wordbag_paht, 'wb')
pickle.dump(bunch, file_obj)
file_obj.close()

print('end')