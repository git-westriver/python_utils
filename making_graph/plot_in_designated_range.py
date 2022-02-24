from matplotlib import pyplot as plt

def count_for_plot(data=[0.1, 0.3, 0.5], left=0, right=1, width=0.1):
    """
    dataの数をカウントしてleftからrightまでの間に間隔widthでプロットする．
    """
    x_num = int((right-left)/width)
    x = [left+ i * width for i in range(x_num)]
    count = [0]*x_num
    for d in data:
        if d > right:
            count[-1] += 1
        elif d < left:
            count[0] += 1
        else:
            count[int((d-left)/width)] += 1

    return x, count

def plot_in_range(data, left, right, width):
    x, count = count_for_plot(data, left, right, width)
    plt.plot(x, count)
    plt.show()