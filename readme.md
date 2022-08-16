# 拼音输入法


### 实验环境

本项目使用python3编写，使用第三方库`chardet`来应对文件编码问题。你可以执行以下指令来安装：

```
$ pip install chardet
```



### 使用方法及参数说明

#### 1.获取提示

```
$ python main.py -h
```

#### 2.预处理

```
$ python main.py -r <chars_file> <pinyin_file> [<save_file>]
$ python main.py -r ../data/pre/chars.txt ../data/pre/pinyin.txt pre.txt
```

* `char_file`：汉字表
* `pinyin_file`：拼音汉字对照表
* `save_file`：保存文件名。这是一个可选参数，默认保存在`main.py`同目录下`pre.txt`

#### 3.训练

```
$ python main.py -t <pre_file> <train_path> [<save_file>]
$ python main.py -t pre.txt ../data/train/ train.txt
```

* `pre_file`：预处理保存下来的文件
* `train_path`：语料库目录名。该目录下仅包含所有训练语料
* `save_file`：保存文件名。这是一个可选参数，默认保存在`main.py`同目录下`train.txt`

#### 4.翻译

翻译有两种模式，分别是命令行输入翻译，文件翻译。

`-i`为命令行输入翻译，输入`q`可退出

```
$ python main.py -s -i <pre_file> <train_file>
$ python main.py -s -i pre.txt train.txt
```

`-f`为文件翻译

```
$ python main.py -s -f <pre_file> <train_file> <input_file> <output_file>
$ python main.py -s -f pre.txt train.txt ../data/input.txt ../data/output.txt
```

* `pre_file`：预处理保存下来的文件
* `train_file`：训练保存下来的模型
* `input_file`：输入拼音文件
* `output_file`：输出转换文件

#### 5.计算准确率

```
$ python main.py -a <file1> <file2>
$ python main.py -a ../data/output.txt ../data/ans.txt
```

#### 6.计算不同参数$\lambda$对准确率影响

```
$ python main.py -l <pre_file> <train_file> <input_file> <output_file> <ans_file>
$ python main.py -l pre.txt train.txt ../data/input.txt ../data/output.txt ../data/ans.txt
```

* `pre_file`：预处理保存下来的文件
* `train_file`：训练保存下来的模型
* `input_file`：输入拼音文件
* `output_file`：输出转换文件
* `ans_file`：标准转换文件



### 目录结构及文件

* `data/`：存放测试数据（输入拼音文件input.txt，转换结果文件output.txt）
* `src/`：存放代码以及预处理后的文件
  * `src/main.py`：主程序，整合了所有代码功能，在命令行中通过参数控制执行功能
  * `src/pre.py`：预处理，创建字表，拼音对照表供训练使用
  * `src/train.py`：使用语料库训练模型，创建字频词频表
  * `src/core.py`：viterbi算法求最短路径，将拼音串转换为汉字串
  * `src/accuracy.py`：计算字准确率和句准确率
  * `src/test_lambda.py`计算不同$\lambda$下字准确率和句准确率

