import numpy as np

# 使用numpy生成数组，得到ndarray类型
# np.array   np.arange
t1 = np.array([1, 2, 3])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)

t3 = np.arange(4, 10, 2)
print(t3)
print(t3.dtype)

# numpy中的数据类型
t4 = np.array(range(1, 4), dtype=float)
print(t4)
print(t4.dtype)

# numpy中的布尔类型
t5 = np.array([1, 1, 0, 1, 0], dtype=bool)
print(t5)

# 调整数据类型
t6 = t5.astype(int)
print(t6)

# numpy中的小数 , 使用random来生成
n7 = np.array([np.random.random() for i in range(10)])
print(n7)

# 取几位小数
n8 = np.round(n7, 2)
print(n8)
