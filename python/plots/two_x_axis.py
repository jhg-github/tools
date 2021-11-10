import numpy as np
import matplotlib.pyplot as plt
fig, ax1 = plt.subplots()
x = [0,1,2,3]
y = [0,1,2,3]
ax1.plot(x, y)
ax1.grid(True)
ax1.set_xlabel("AX1")
ax2 = ax1.twiny()
ax2.set_xticks( ax1.get_xticks() )
ax2.set_xbound(ax1.get_xbound())
ax2.set_xticklabels([x * 2 for x in ax1.get_xticks()])
ax2.set_xlabel("AX2")
plt.show()
