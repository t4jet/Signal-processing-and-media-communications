import numpy as np
import matplotlib.pyplot as plt

# 与えられたフーリエ級数の係数
a0 = 3
a1 = 2
a2 = -4
a3 = -1
b1 = -3
b2 = 5
b3 = 2

# 時間の範囲を設定（1周期のため0から2πまで）
t = np.linspace(0, 2 * np.pi, 1000)

# フーリエ級数の計算
f_t = a0 + a1 * np.cos(t) + a2 * np.cos(2 * t) + a3 * np.cos(3 * t) \
     + b1 * np.sin(t) + b2 * np.sin(2 * t) + b3 * np.sin(3 * t)

# 信号f(t)のプロット
plt.figure(figsize=(10, 6))
plt.plot(t, f_t, label='f(t)', color='blue')
plt.title('Signal f(t) formed by Fourier Series')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid(True)
plt.legend()
plt.show()


print("Fourier coefficients:")
print(f"a0 = {a0}")
print(f"a1 = {a1}")
print(f"a2 = {a2}")
print(f"a3 = {a3}")
print(f"b1 = {b1}")
print(f"b2 = {b2}")
print(f"b3 = {b3}")
