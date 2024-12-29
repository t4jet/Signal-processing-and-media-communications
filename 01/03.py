import numpy as np
import matplotlib.pyplot as plt

# フーリエ級数の係数
a0 = 3.0
a1 = 2.0
a2 = -4.0
a3 = -1.0
b1 = -3.0
b2 = 5.0
b3 = 2.0

#信号
def f(t):
    return ( a0 / 2 +
            a1 * np.cos(2 * np.pi * 1 * t ) + b1 * np.sin(2 * np.pi * 1 * t)+
            a2 * np.cos(2 * np.pi * 2 * t) + b2 * np.sin(2 * np.pi * 2 * t) +
            a3 * np.cos(2 * np.pi * 3 * t) + b3 * np.sin(2 * np.pi * 3 * t))

# 時間の範囲
t = np.linspace(0, 1, 1000)  # 0から1秒まで1000点

# 信号を計算
signal = f(t)

# 信号をプロット
plt.plot(t, signal)
plt.title('graph')
plt.xlabel('Time (s)')
plt.ylabel('f(t)')
plt.grid()
plt.show()