import matplotlib.pyplot as plt
import math
import array as arr

op = input("What exponent? ")

if op == "1":
  m = float(input("m: "))
  d = float(input("d: "))

  for i in range (5):
    y = m*i+d
    ax.append(i)
    ay.append(y)


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

#Use quadratic formula to determine x-ints
x1 = (-b + math.sqrt(b**2-4*a*c))/2*a
x2 = (-b - math.sqrt(b**2-4*a*c))/2*a
print(str(x1) + " and " + str(x2))

 #a = arr.array([0],[c])
z=0

#Create a x & y value array to make table of values
ax = arr.array("i", [0])
ay = arr.array("i", [c])

#go up to x=5 and get y value in order to graph
for i in range (5):
  y = (a*i)**2+b*i+c
  ax.append(i)
  ay.append(y)
        
plt.plot(ax, ay, label = "line 1")
plt.show()
