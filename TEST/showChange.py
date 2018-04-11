# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *     
import math                            #支持中文
def show_picture(*state):
    mpl.rcParams['font.sans-serif'] = ['SimHei']

    names = ['5', '10', '15', '20', '25']
    x = range(len(state))
    y = state
    plt.plot(x, y)
    plt.legend()  # 让图例生效
    plt.margins(0)
    plt.xlabel("time") #X轴标签
    plt.ylabel("RMSE") #Y轴标签
    plt.title("A simple plot") #标题
    # plt.show()
    plt.savefig("easyplot.jpg")  
if __name__ =="__main__":
    state=[]
    for i in range(50):
        state.append(math.sin(i))
    # print(state)
    show_picture(*state)

