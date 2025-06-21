# Mathew McKee
# 6/21/2025
# P2LAB1
# calculate diameter, circumference, and area of a circle using a float input as radius
import math

radius = float(input("What is the radius of the circle? "))
print()
diameter = float(radius * 2)
circumference = float(2 * math.pi * radius)
area = float(math.pi * radius * radius)
print(f"The diameter of the circle is {diameter:.1f}\n")
print(f"The circumference of the circle is {circumference:.2f}\n")
print(f"The area of the circle is {area:.3f}")
