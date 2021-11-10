import matplotlib.pyplot as plt


x = [ [1,2,3], [1,4 ,7] ]
y = [ [2,2.1,2.2], [3,3.1,3.2] ]
labels = ['cdc','kol']
for i in range(len(x)):
    plt.plot(x[i],y[i], label=labels[i])
plt.legend()
plt.show()

