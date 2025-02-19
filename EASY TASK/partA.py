import matplotlib.pyplot as plt
x_values=[]
y_values=[]
n=eval(input("enter the number of points to be plottted"))
# to append user inputted data into the list for x and y coordinates
for i in range(n):
    x=eval(input("enter value for x co ordinate[%d]: "%(i+1)))
    y=eval(input("enter value for y co ordinate[%d]: "%(i+1)))
    x_values.append(x)
    y_values.append(y) 
plt.plot(x_values,y_values)
plt.show()