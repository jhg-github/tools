import matplotlib.pyplot as plt
fig = plt.figure()

ax_raw = plt.subplot2grid((2, 2), (0, 0), colspan=2)
ax_raw.set_title('Raw')

ax_flow = plt.subplot2grid((2, 2), (1, 0))
ax_flow.set_title('Flow')

ax_vol = plt.subplot2grid((2, 2), (1, 1))
ax_vol.set_title('Volume')

plt.tight_layout()
plt.show()