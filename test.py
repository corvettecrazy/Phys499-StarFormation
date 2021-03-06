print('hello')#displays the word hello in the command window
a=3
print(a) #displays the variable a in the command window

import numpy as np  #imports numpy toolbox (trig functions, logs, etc.)
import matplotlib.pyplot as plt #importing plot toolbox
x=np.linspace(-2*np.pi,2*np.pi,1001) #builds a range of x values from -2pi to 2pi with 1001 points in between
y=np.sin(x) #define sin. Need to specify np.sin to draw it from the numpy toolbox which we defined as np
z=np.cos(x) #define cos. Need to specify np.cos to draw it from the numpy toolbox
plt.plot(x,y) #builds a plot of x Vs. sin(x). Need to specift plt from matplotlib toolbox
plt.plot(x,z) #builds a plot of x vs. cos(x) on the same plot as above
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('graph of sin and cos')
#plt.show() #displays the plot above. If line is not present in code, manually type this into command line to display
y=np.matrix('1 2 3;3 4 5;7 8 9') #builds a 3x3 matrix
word='taint'
print(word)
