from bert_serving.client import BertClient
import numpy as np

puncs = [']', '[', '（', '）', '{', '}', '：', '《', '》']  # 将数据中的一些中文符号去除
files_content = ''
with open('../Datasets/poetry_7_1_(wufuhao).txt', 'r', encoding='utf-8') as f:
    for line in f:
        # 每行的末尾加上"]"符号代表一首诗结束
        for char in puncs:
            line = line.replace(char, "")  # 处理无关的字符
        files_content += line.strip() + "\n"  # 去除一行中首尾的空格符

bc = BertClient()
num = 0
tmp = []
data = files_content.split("\n")
print(len(data))
for line in data:
    text = ''
    i = 0
    for item in line:
        i += 1
        if i == 7:
            break
        if item == '\n':
            continue
        text += item
        tmp.append(bc.encode([text]))
    num += 1
    if num%100==0:
        print(num)

predictors = np.array(tmp)
print(predictors.shape)
np.save('../Datasets/predictors', predictors)
