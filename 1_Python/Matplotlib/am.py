import matplotlib.pyplot as plt
import numpy as np

# Create a 3D scatter plot
fig3 = plt.figure()
ax = fig3.add_subplot(111, projection='3d')

# Data
z = 20 * np.random.random(100)  # Random values for z
x = np.sin(z)
y = np.cos(z)

# Plotting
ax.scatter(x, y, z, c=z, cmap='Blues')  # Color by z values
ax.set_title('3D Scatter Plot')
ax.set_xlabel('X axis (sin)')
ax.set_ylabel('Y axis (cos)')
ax.set_zlabel('Z axis')

# Display the plot
plt.show()
