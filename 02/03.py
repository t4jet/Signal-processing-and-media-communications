import numpy as np
import matplotlib.pyplot as plt

# n の範囲を定義
nbegin = -5
nend = 10
n = np.arange(nbegin, nend + 1, 1)

# 指数関数を定義
exp_function = np.where(n >= 0, np.exp(-n/4), 0)

# プロット
fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
ax1.stem(n, exp_function, basefmt=" ")

# 軸の設定
ax1.set_xlim(nbegin, nend)
ax1.set_ylim(-0.2, 1.2)
ax1.grid(True)

# ラベルの設定
ax1.set_xlabel('Time $n$')
ax1.set_ylabel('$a[n]$')

# プロットを表示
plt.show()
