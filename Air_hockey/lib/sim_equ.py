
import matplotlib.pyplot as plt
import numpy as np
# 準備數據 ... 假設我要畫一個sin波 從0~180度

x1 = 32
y1 = 54
x2 = 34
y2 = 59
m = (y2-y1)/(x2-x1)
x = np.arange(0,180)
y = m*(x-x1)


# 開始畫圖

    # 設定要畫的的x,y數據list....

plt.plot(x,y)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("The Title")


    # 在這個指令之前，都還在做畫圖的動作
    # 這個指令算是 "秀圖"
plt.show()



"""
x1 = 32
y1 = 54
x2 = 34
y2 = 59
m = (y2-y1)/(x2-x1)
y = m*(x-x1)
"""