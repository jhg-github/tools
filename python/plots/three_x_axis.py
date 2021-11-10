
import matplotlib.pyplot as plt 
fig, host = plt.subplots(figsize=(8,5)) # (width, height) in inches
par1 = host.twiny()
par2 = host.twiny()     
host.set_xlabel("AX1")
host.set_ylabel("AY1")
par1.set_xlabel("AX2")
par2.set_xlabel("AX3")
p1, = host.plot([0, 1, 2], [0, 1, 2])
par2.spines['top'].set_position(('outward', 35))

par1.set_xticks( host.get_xticks() )
par1.set_xbound( host.get_xbound())
par1.set_xticklabels([x * 2 for x in host.get_xticks()])

par2.set_xticks( host.get_xticks() )
par2.set_xbound( host.get_xbound())
par2.set_xticklabels([x * 3 for x in host.get_xticks()])

host.grid(True)

fig.tight_layout()
plt.show()

# original example
# import matplotlib.pyplot as plt 
# # Create figure and subplot manually
# # fig = plt.figure()
# # host = fig.add_subplot(111)
# # More versatile wrapper
# fig, host = plt.subplots(figsize=(8,5)) # (width, height) in inches
# # (see https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.subplots.html)    
# par1 = host.twinx()
# par2 = host.twinx()    
# host.set_xlim(0, 2)
# host.set_ylim(0, 2)
# par1.set_ylim(0, 4)
# par2.set_ylim(1, 65)    
# host.set_xlabel("Distance")
# host.set_ylabel("Density")
# par1.set_ylabel("Temperature")
# par2.set_ylabel("Velocity")
# color1 = plt.cm.viridis(0)
# color2 = plt.cm.viridis(0.5)
# color3 = plt.cm.viridis(.9)
# p1, = host.plot([0, 1, 2], [0, 1, 2],    color=color1, label="Density")
# p2, = par1.plot([0, 1, 2], [0, 3, 2],    color=color2, label="Temperature")
# p3, = par2.plot([0, 1, 2], [50, 30, 15], color=color3, label="Velocity")
# lns = [p1, p2, p3]
# host.legend(handles=lns, loc='best')
# # right, left, top, bottom
# par2.spines['right'].set_position(('outward', 60))
# # Sometimes handy, same for xaxis
# # par2.yaxis.set_ticks_position('right')
# # Move "Velocity"-axis to the left
# # par2.spines['left'].set_position(('outward', 60))
# # par2.spines['left'].set_visible(True)
# # par2.yaxis.set_label_position('left')
# # par2.yaxis.set_ticks_position('left')
# host.yaxis.label.set_color(p1.get_color())
# par1.yaxis.label.set_color(p2.get_color())
# par2.yaxis.label.set_color(p3.get_color())
# # Adjust spacings w.r.t. figsize
# fig.tight_layout()
# # Alternatively: bbox_inches='tight' within the plt.savefig function 
# #                (overwrites figsize)
# plt.show()