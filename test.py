#Labb 3 förberedelser

import numpy as np
import matplotlib.pyplot as plt


unlabelled_data = np.genfromtxt(r"C:\Python\Labb3\unlabelled_data.csv", delimiter=",")
print(unlabelled_data)
plt.scatter(unlabelled_data[:,0], unlabelled_data[:,1])

line_x = np.array([-5,5])

plt.plot(line_x, -line_x)
plt.show()