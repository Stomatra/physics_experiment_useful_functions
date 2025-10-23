"""
physics_uncertainty.py
----------------------
用于物理学实验数据处理的工具库，包含平均值计算、不确定度分析（A类、B类、合成不确定度）等功能。

核心功能：
- 普通平均值、逐差法平均值计算
- A类不确定度（含t分布校正）、B类不确定度计算
- 相对不确定度、合成不确定度计算

使用示例：
data = [1.2, 1.3, 1.4]
avg = normal_avg(data)
type_a = type_a_uncertainty(data, avg)
print(f"平均值：{avg:.2f}，A类不确定度：{type_a:.2f}")
"""

def t_P(list,P=0.683):
    '''
    获取给定列表长度和置信水平对应的 t 值。
    参数：
        list (list): 数值型数据的列表。
        P (float): 置信水平（默认为 0.683）。
    返回：
        float: 对应于列表长度和置信水平的 t 值。

    Get the t-value for a given list size and confidence level.
    Args:
        list (list): A list of numerical values.
        P (float): The confidence level (default is 0.683).
    Returns:
        float: The t-value corresponding to the list size and confidence level.
    '''
    n=len(list)
    n_list=[3,4,5,6,7,8,9,10,15,20]
    P_list=[0.90,0.95,0.99,0.683]
    data = [
    [2.92, 2.35, 2.13, 2.02, 1.94, 1.90, 1.86, 1.83, 1.76, 1.73],
    [4.30, 3.38, 2.78, 2.57, 2.46, 2.37, 2.31, 2.26, 2.15, 2.09],
    [9.93, 5.84, 4.60, 4.03, 3.71, 3.50, 3.36, 3.25, 2.98, 2.86],
    [1.32, 1.20, 1.14, 1.11, 1.09, 1.08, 1.07, 1.06, 1.04, 1.03]
    ]
    if n in n_list and P in P_list:
        row = P_list.index(P)
        col = n_list.index(n)
        return data[row][col]
    else:
        raise ValueError("The provided list length or confidence level is not supported.")

def normal_avg(list):
    '''
    计算数值列表的普通平均值。
    参数：
        list (list): 数值型数据的列表。
    返回：
        float: 列表的平均值。

    Calculate the normal average of a list of numbers.
    Args:
        list (list): A list of numerical values.
    Returns:
        float: The average of the list.
    '''
    return sum(list) / len(list)

def successive_difference_method_avg(list):
    '''
    计算数值列表的逐差法平均值。
    参数：
        list (list): 数值型数据的列表。
    返回：
        float: 列表的平均值。

    Calculate the average using the successive difference method.
    Args:
        list (list): A list of numerical values.
    Returns:
        float: The average of the list.
    '''
    n = len(list)
    half=n//2
    diffs = [abs(list[i+half] - list[i]) for i in range(n - half)]
    return sum(diffs) / len(diffs) if diffs else 0

def standard_deviation(list, avg):
    '''
    计算数值列表的样本标准偏差。
    参数：
        list (list): 数值型数据的列表。
        avg (float): 列表的平均值。
    返回：
        float: 列表的样本标准偏差。

    Calculate the standard deviation of a list of numbers.
    Args:
        list (list): A list of numerical values.
        avg (float): The average of the list.
    Returns:
        float: The standard deviation of the list.
    '''
    n = len(list)
    variance = sum((x - avg) ** 2 for x in list) / (n - 1)
    return variance ** 0.5

def type_a_uncertainty(list, avg,P=0.683):
    '''
    计算一组数据的 A 类不确定度。
    参数：
        list (list): 数值型数据的列表。
        avg (float): 列表的平均值。
    返回：
        float: A 类不确定度。

    Calculate the Type A uncertainty of a list of numbers.
    Args:
        list (list): A list of numerical values.
        avg (float): The average of the list.
    Returns:
        float: The Type A uncertainty.
    '''
    n = len(list)
    if n < 2:
        return 0
    std_dev = standard_deviation(list, avg)
    t_value = t_P(list,P)
    return t_value * std_dev / (n ** 0.5)

def type_b_uncertainty(instrument_uncertainty):
    '''
    计算 B 类不确定度。
    参数：
        instrument_uncertainty (float): 测量仪器的不确定度。
    返回：
        float: B 类不确定度。

    Calculate the Type B uncertainty.
    Args:
        instrument_uncertainty (float): The uncertainty of the measuring instrument.
    Returns:
        float: The Type B uncertainty.
    '''
    return instrument_uncertainty / (3 ** 0.5)

def relative_uncertainty(value, uncertainty):
    '''
    计算相对不确定度。
    参数：
        value (float): 测量值。
        uncertainty (float): 测量值的不确定度。
    返回：
        float: 相对不确定度。

    Calculate the relative uncertainty.
    Args:
        value (float): The measured value.
        uncertainty (float): The uncertainty of the measured value.
    Returns:
        float: The relative uncertainty.
    '''
    return uncertainty / value if value != 0 else 0

def combined_uncertainty(type_a, type_b):
    '''
    计算由 A 类和 B 类的合成不确定度。
    参数：
        type_a (float): A 类不确定度。
        type_b (float): B 类不确定度。
    返回：
        float: 合成不确定度。

    Calculate the combined uncertainty.
    Args:
        type_a (float): The Type A uncertainty.
        type_b (float): The Type B uncertainty.
    Returns:
        float: The combined uncertainty.
    '''
    return (type_a ** 2 + type_b ** 2) ** 0.5

def directly_calculated_combined_uncertainty(list,avg,type_b=None,*,instrument_uncertainty=None,P=0.683):
    '''
    计算直接计算值的合成不确定度。
    instrument_uncertainty 和 type_b 二选一提供。
    参数：
        list (list): 数值型数据的列表。
        avg (float): 列表的平均值。
        instrument_uncertainty (float): 测量仪器的不确定度。
    返回：
        float: 合成不确定度。

    Calculate the combined uncertainty for directly calculated values.
    instrument_uncertainty and type_b are mutually exclusive.
    Args:
        list (list): A list of numerical values.
        avg (float): The average of the list.
        instrument_uncertainty (float): The uncertainty of the measuring instrument.
    Returns:
        float: The combined uncertainty.
    '''
    if type_b and instrument_uncertainty is None:
        raise ValueError("Either type_b or instrument_uncertainty must be provided.")
    elif type_b and instrument_uncertainty is not None:
        raise ValueError("Provide either type_b or instrument_uncertainty, not both.")
    elif instrument_uncertainty is not None:
        type_b = type_b_uncertainty(instrument_uncertainty)
    type_a = type_a_uncertainty(list, avg,P)
    return combined_uncertainty(type_a, type_b)