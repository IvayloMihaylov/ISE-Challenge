import string
import os
import sys

fuel = 0
total_fuel = 0

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

# Get the absolute path for the project / repository root
pathroot = os.path.abspath(os.path.join(here, ".."))

with open(pathroot + "/Module_masses.txt", "r") as f:
    for mass in f:
#        print("Module mass", mass)
#        print('Fuel needed for this module', int(mass)//3-2)
        f= open("fuel.txt","a+")
        f.write("%d\r\n" % (int(mass)//3-2))
        total_fuel = total_fuel + int(mass) + 1
        print("Needed so far", total_fuel)       

print("All the fuel you need is", total_fuel)