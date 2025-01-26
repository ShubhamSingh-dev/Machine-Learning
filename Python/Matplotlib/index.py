# Matplotlib is used for plotting graphs
# Matplotlib is a Python library for creating static, animated, and interactive visualizations in Python.

import matplotlib.pyplot as plt
import numpy as np  # Importing numpy to get data for our plots

# Generate data for plots
x = np.linspace(0, 10, 100)  # Creating 100 points from 0 to 10
y = np.sin(x)  # Creating a sine wave
z = np.cos(x)  # Creating a cosine wave

# Plot sine wave
plt.plot(x, y)
plt.title("Sine wave")
plt.xlabel("Angle")
plt.ylabel("Sine value")
plt.show()

# Plot cosine wave
plt.plot(x, z)
plt.title("Cosine wave")
plt.xlabel("Angle")
plt.ylabel("Cosine value")
plt.show()

# Plot a parabola
x = np.linspace(-10, 10, 20)
y = x**2
plt.plot(x, y)
plt.title("Parabola")
plt.xlabel("x")
plt.ylabel("x squared")
plt.show()

# Plot parabola with different colors and markers
plt.plot(x, y, "r+", label="Red +")  # r+ for red color and plus markers
plt.plot(x, y, "g*", label="Green *")  # g* for green color and star markers
plt.plot(x, y, "b--", label="Blue --")  # b-- for blue color and dashed line
plt.title("Parabola with different styles")
plt.legend()
plt.show()

# Create a multi-line plot
x = np.linspace(-5, 5, 50)
plt.plot(x, np.sin(x), "g-", label="Sine")  # Green solid line for sine
plt.plot(x, np.cos(x), "r--", label="Cosine")  # Red dashed line for cosine
plt.title("Sine and Cosine Waves")
plt.xlabel("x")
plt.ylabel("Value")
plt.legend()
plt.show()

# Create a bar plot
fig, ax = plt.subplots()
languages = ['Python', 'Java', 'C++', 'C', 'C#']
popularity = [22.2, 17.6, 8.8, 8, 7.7]
ax.bar(languages, popularity)
ax.set_xlabel('Languages')
ax.set_ylabel('Popularity')
ax.set_title('Popularity of Programming Languages')
plt.show()

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(popularity, labels=languages, autopct='%1.1f%%')
ax.set_title('Popularity of Programming Languages')
plt.show()

# Create a scatter plot
x = np.linspace(0, 10, 30)
y = np.sin(x)
z = np.cos(x)
fig2, ax = plt.subplots()
ax.scatter(x, y, color="green", label="Sine")  # Green scatter for sine
ax.scatter(x, z, color="red", label="Cosine")  # Red scatter for cosine
ax.set_title('Scatter Plot')
ax.legend()
plt.show()

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

