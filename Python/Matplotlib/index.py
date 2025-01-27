# Matplotlib: A Python library for creating static, animated, and interactive visualizations.

import matplotlib.pyplot as plt  # For creating plots
import numpy as np  # For generating data for plots

# Generate data for plotting
x = np.linspace(0, 10, 100)  # Generate 100 evenly spaced points between 0 and 10
y = np.sin(x)  # Sine values for the x points
z = np.cos(x)  # Cosine values for the x points

# SIMPLE LINE PLOTS
# 1. Plotting a sine wave
plt.plot(x, y)  # Create a line plot of sine values
plt.title("Sine wave")  # Add a title to the plot
plt.xlabel("Angle")  # Label for the x-axis
plt.ylabel("Sine value")  # Label for the y-axis
plt.show()  # Display the plot

# 2. Plotting a cosine wave
plt.plot(x, z)  # Create a line plot of cosine values
plt.title("Cosine wave")  # Add a title to the plot
plt.xlabel("Angle")  # Label for the x-axis
plt.ylabel("Cosine value")  # Label for the y-axis
plt.show()  # Display the plot

# PARABOLA PLOTS
# 3. Plotting a parabola
x = np.linspace(-10, 10, 20)  # Generate 20 points between -10 and 10
y = x**2  # Square the x values to create parabola data
plt.plot(x, y)  # Plot the parabola
plt.title("Parabola")  # Add a title
plt.xlabel("x")  # Label for the x-axis
plt.ylabel("x squared")  # Label for the y-axis
plt.show()  # Display the plot

# 4. Plotting parabola with different styles
plt.plot(x, y, "r+", label="Red +")  # Red color with plus markers
plt.plot(x, y, "g*", label="Green *")  # Green color with star markers
plt.plot(x, y, "b--", label="Blue --")  # Blue dashed line
plt.title("Parabola with different styles")  # Add a title
plt.legend()  # Add a legend to differentiate styles
plt.show()  # Display the plot

# MULTI-LINE PLOTS
# 5. Plotting sine and cosine waves together
x = np.linspace(-5, 5, 50)  # Generate 50 points between -5 and 5
plt.plot(x, np.sin(x), "g-", label="Sine")  # Green solid line for sine
plt.plot(x, np.cos(x), "r--", label="Cosine")  # Red dashed line for cosine
plt.title("Sine and Cosine Waves")  # Add a title
plt.xlabel("x")  # Label for the x-axis
plt.ylabel("Value")  # Label for the y-axis
plt.legend()  # Add a legend
plt.show()  # Display the plot

# BAR PLOT
# 6. Creating a bar plot for programming language popularity
fig, ax = plt.subplots()  # Create a figure and axes
languages = ['Python', 'Java', 'C++', 'C', 'C#']  # Categories
popularity = [22.2, 17.6, 8.8, 8, 7.7]  # Values
ax.bar(languages, popularity)  # Create a bar plot
ax.set_xlabel('Languages')  # Label for the x-axis
ax.set_ylabel('Popularity')  # Label for the y-axis
ax.set_title('Popularity of Programming Languages')  # Add a title
plt.show()  # Display the plot

# PIE CHART
# 7. Creating a pie chart for programming language popularity
fig, ax = plt.subplots()  # Create a figure and axes
ax.pie(popularity, labels=languages, autopct='%1.1f%%')  # Create a pie chart with percentage values
ax.set_title('Popularity of Programming Languages')  # Add a title
plt.show()  # Display the plot

# SCATTER PLOT
# 8. Creating a scatter plot for sine and cosine values
x = np.linspace(0, 10, 30)  # Generate 30 points between 0 and 10
y = np.sin(x)  # Sine values
z = np.cos(x)  # Cosine values
fig2, ax = plt.subplots()  # Create a figure and axes
ax.scatter(x, y, color="green", label="Sine")  # Green scatter for sine
ax.scatter(x, z, color="red", label="Cosine")  # Red scatter for cosine
ax.set_title('Scatter Plot')  # Add a title
ax.legend()  # Add a legend
plt.show()  # Display the plot

# 3D SCATTER PLOT
# 9. Creating a 3D scatter plot
fig3 = plt.figure()  # Create a figure
ax = fig3.add_subplot(111, projection='3d')  # Add 3D axes to the figure

# Generating random data for 3D plot
z = 20 * np.random.random(100)  # Random values for z-axis
x = np.sin(z)  # Sine values for x-axis
y = np.cos(z)  # Cosine values for y-axis

# Creating the scatter plot
ax.scatter(x, y, z, c=z, cmap='Blues')  # Points colored by z values, using the 'Blues' colormap
ax.set_title('3D Scatter Plot')  # Add a title
ax.set_xlabel('X axis (sin)')  # Label for x-axis
ax.set_ylabel('Y axis (cos)')  # Label for y-axis
ax.set_zlabel('Z axis')  # Label for z-axis

plt.show()  # Display the plot
