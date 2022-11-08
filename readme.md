**本项目主要实现了一个自动生成七言古诗词的项目**

- **chinese_L_12-H-768_A-12**

  - Google 发布的预训练的中文的Bert模型
  - 下载连接https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip

- **code**

  - BiGRU-LSTM_wufuhao.ipynb  ：BiGRU+LSTM模型     

  - LSTM-LSTM_wufuhao.ipynb   ：LSTM+LSTM模型

  - BiLSTM-LSTM_wufuhao.ipynb：BiLSTM+LSTM模型

  - Bert-BiGRU-LSTM_wufuhao.ipynb：Bert+BiGRU+LSTM模型

  - Bert-LSTM-LSTM_wufuhao.ipynb：Bert+LSTM+LSTM模型

  - Bert-BiLSTM-LSTM_wufuhao.ipynb：Bert+BiLSTM+LST模型

  - data_gen.py: 预生成的bert词向量数据

  - data-op.py ：数据预处理

  - textSimilar.ipynb: 计算文本相似度

  - **run**：

    - 前六个.ipynb 在Python = 3.8 keras = 2.4.3 tensorflow = 2.5.0 transformers =4.24.0 环境下直接利用jupyter 下运行即可

    - data_gen.py  在Python = 3.6 tensorflow 1.X(X>=10 X<= 15) bert-serving-server、bert-serving-client，并且利用使用 `bert-serving-start` 命令启动服务：**bert-serving-start -model_dir /tmp/english_L-12_H-768_A-12/ -num_worker=2** 其中，`-model_dir` 是预训练模型的路径，`-num_worker` 是线程数，表示同时可以处理多少个并发请求

    - data-op.py 在Python = 3.8 即可运行

    - textSimilar.ipynb 在python 3.6 下载text2vec（会自动下载其他依赖包）、torch库下可以运行

      

- **Datasets**

  - poetry_7.txt: 原始数据集
  - peotry_7_1_(wufuhao).txt: 处理过后数据集
  - predictors.npy: 预生成的bert词向量数据

- **model**

  - BiGRU+LSTM_wufuhao.h5  ：BiGRU+LSTM训练保存模型
  - LSTM+LSTM_wufuhao.h5   ：LSTM+LSTM训练保存模型
  - BiLSTM+LSTM_wufuhao.h5：BiLSTM+LSTM训练保存模型
  - Bert+BiGRU+LSTM_wufuhao.h5：Bert+BiGRU+LSTM训练保存模型
  - Bert+LSTM+LSTM_wufuhao.h5：Bert+LSTM+LSTM训练保存模型
  - Bert+BiLSTM+LSTM_wufuhao.h5：Bert+BiLSTM+LSTM训练保存模型

- **output**

  - 12张.png 图片，为项目中所搭建两种基本模型的训练效果
  - 模型汇总.xlsx 表格文件 存放模型的训练效果的汇总

- **论文**

  - word版NLP课程报告
  - Pdf版NLP课程报告

  