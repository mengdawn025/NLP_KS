
data = open(r'D:\自然语言处理\NLP_KS\Datasets\poetry_7.txt',encoding="utf-8").readlines()

# f  = open('D:\自然语言处理\实验3\content2.txt',"w+")
# i = 0
# for line in data:
#     tmp  = ""
#     for item in line:
#         if item == "\n":
#             continue
#         if item == '，' or item == '。':
#             tmp += "\n"
#             continue
#         tmp += item
#     f.write(tmp)
#     i += 1
#     if i >= 1000 :
#         break
# f.close()

f  = open('D:\\自然语言处理\\NLP_KS\\Datasets\\poetry_7_1_1(wufuhao).txt',"w+",encoding="utf-8")
i = 0
for line in data:
    tmp = ""
    num = 0
    for item in line:
        tmp += item
        num += 1
        if num == 8:
            f.write(tmp[:-1]+"\n")
            print
            num = 0
            tmp = ""
    i += 1
    if i >= 1000:
        break
            
   
f.close()
# print(data[0:14])
# import numpy as np
# x_vec = np.zeros(
#                 shape=(1, 6),
#                 dtype=np.int32
#             )
