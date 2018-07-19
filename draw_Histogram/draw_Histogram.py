import numpy as np
import matplotlib.pyplot as plt

n = 3
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
label = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
color1 = []
color2 = []
for y1, y2 in zip(Y1, Y2):
	if y1 > y2:
		color1.append("lime")
		color2.append("grey")
	else:
		color1.append("grey")
		color2.append("lime")
plt.barh(X, +Y1, color = color1, edgecolor='white')
plt.barh(X, -Y2, color = color2, edgecolor='white')

for x,y in zip(X,Y1):
    plt.text(y+0.1, x-0.3, '%.2f' % y, ha='center', va= 'bottom')
for x,y in zip(X,Y2):
    plt.text(-(y+0.1), x-0.3, '%.2f' % y, ha='center', va= 'bottom')
for x,y in zip(X,label):
    plt.text(-1.5, x-0.3, '%.2f' % y, ha='center', va= 'bottom')
plt.xlim(-1.75,+1.25)
plt.show()