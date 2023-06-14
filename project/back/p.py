import matplotlib.pyplot as plt

# Create the figures and plots
fig1, ax1 = plt.subplots()
ax1.plot(1, 5)
ax1.set_title('Figure 1')

fig2, ax2 = plt.subplots()
ax2.plot(2, 6)
ax2.set_title('Figure 2')

# Show the first figure
plt.show(block=False)

# Enable the navigation toolbar
plt.rcParams['toolbar'] = 'toolbar2'

# Navigate to the next figure
plt.figure(fig1.number)
plt.get_current_fig_manager().toolbar.next()

# Navigate to the previous figure
plt.figure(fig2.number)
plt.get_current_fig_manager().toolbar.back()

# Show the second figure
plt.show()
