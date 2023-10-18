Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> # Get the diameter and price from the user
>>> diameter = float(input("Enter the diameter of the pizza in inches: "))
Enter the diameter of the pizza in inches: 8
>>> price = float(input("Enter the price of the pizza: "))
Enter the price of the pizza: 34.99
>>> # Calculate the radius
>>> radius = diameter / 2
>>> # Calculate the area
>>> area = math.pi * (radius**2)
>>> # Calculate the cost per square inch
>>> cost_per_square_inch = price / area
