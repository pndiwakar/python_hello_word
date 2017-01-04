#!bin/python

# Impoort the required module for getting maths function PI
from math import pi

#assign the input to variable
r = float(input("Input the radius of circle : "))
# To make it square of r either use "r * r" or "r**2"
print ("Areas of circle with radius={} is : {}" .format(r, str(pi * (r * r))))

