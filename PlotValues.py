from matplotlib import pyplot as pt

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 1, 5, 2, 6]

pt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
        marker='o', markerfacecolor='blue', markersize=12)

pt.title('Epic chart')
pt.ylabel('Y-axis')
pt.xlabel('X-axis')

pt.show()