import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np



# def z_function(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(0, 2, 3)
y = np.linspace(0, 2,3)
X, Y = np.meshgrid(x, y)
# Z = z_function(X, Y)
Z = np.zeros((3,3))
print(Z)
Z[1][1]=1
Z[1][2]=1
print(Z)

fig = plt.figure()
ax = plt.axes(projection="3d")
# ax.plot_wireframe(X, Y, Z, color='green')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='winter', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()


# xvalues = np.array([0, 1, 2])
# yvalues = np.array([0, 1, 2])
# xx, yy = np.meshgrid(xvalues, yvalues)
# z = xx
# z[0,0] = 0
# z[0,1] = 0
# z[0,2] = 0
# z[1,0] = 0
# z[1,1] = 1
# z[1,2] = 0
# z[2,0] = 0
# z[2,1] = -1
# z[2,2] = 0
# ax = plt.axes(projection='3d')
# ax.plot_surface(xx, yy, z, rstride=1, cstride=1,
#                 cmap='viridis', edgecolor='none')
# print(z)

# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# # Make data.
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# Z = X
# # Plot the surface.
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# # Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# # A StrMethodFormatter is used automatically
# ax.zaxis.set_major_formatter('{x:.02f}')
# # Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()