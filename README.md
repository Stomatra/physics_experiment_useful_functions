# physics_experiment_useful_functions
为了应付大物实验的各种平均值，不确定度的计算，一个个的弄都要折磨疯了，索性直接写了个库函数来计算
## 导入方法
把文件下载或者复制下来，放到需要的文件的同一目录下，若下载建议重命名文件，之后可以直接导入，如下：
```py
import your_filename
import your_filename as fn
```
## 函数介绍
### 获取给定列表长度和置信水平对应的 t 值
```py
t_P(list,P=0.683):
    获取给定列表长度和置信水平对应的 t 值。
    参数：
        list (list): 数值型数据的列表。
        P (float): 置信水平（默认为 0.683）。
    返回：
        float: 对应于列表长度和置信水平的 t 值。
```
### 计算数值列表的普通平均值。
```py
normal_avg(list):
    计算数值列表的普通平均值。
    参数：
        list (list): 数值型数据的列表。
    返回：
        float: 列表的平均值。
```
### 计算数值列表的逐差法平均值。
```py
successive_difference_method_avg(list):
    计算数值列表的逐差法平均值。
    参数：
        list (list): 数值型数据的列表。
    返回：
        float: 列表的平均值。
```
### 计算数值列表的样本标准偏差。
```py
standard_deviation(list, avg):
    计算数值列表的样本标准偏差。
    参数：
        list (list): 数值型数据的列表。
        avg (float): 列表的平均值。
    返回：
        float: 列表的样本标准偏差。
```
### 计算一组数据的 A 类不确定度。
```py
type_a_uncertainty(list, avg,P=0.683):
    计算一组数据的 A 类不确定度。
    参数：
        list (list): 数值型数据的列表。
        avg (float): 列表的平均值。
    返回：
        float: A 类不确定度。
```
### 计算 B 类不确定度。
```py
type_b_uncertainty(instrument_uncertainty):
    计算 B 类不确定度。
    参数：
        instrument_uncertainty (float): 测量仪器的不确定度。
    返回：
        float: B 类不确定度。
```
### 计算相对不确定度。
```py
relative_uncertainty(value, uncertainty):
    计算相对不确定度。
    参数：
        value (float): 测量值。
        uncertainty (float): 测量值的不确定度。
    返回：
        float: 相对不确定度。
```
### 计算由 A 类和 B 类的合成不确定度。
```py
combined_uncertainty(type_a, type_b):
    计算由 A 类和 B 类的合成不确定度。
    参数：
        type_a (float): A 类不确定度。
        type_b (float): B 类不确定度。
    返回：
        float: 合成不确定度。
```
### 计算直接计算值的合成不确定度。
```py
directly_calculated_combined_uncertainty(list,avg,type_b=None,*,instrument_uncertainty=None,P=0.683):
    '''
    计算直接计算值的合成不确定度。
    instrument_uncertainty 和 type_b 二选一提供。
    参数：
        list (list): 数值型数据的列表。
        avg (float): 列表的平均值。
        instrument_uncertainty (float): 测量仪器的不确定度。
    返回：
        float: 合成不确定度。
```
