Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def main():
...     X1,X2=eval(input("Enter x coordinates:"))
...     Y1,Y2=eval(input("Enter y coordinates:"))
...     distance=math.sqrt((X2-X1)**2+(Y2-Y1)**2)#calculating distance
...     print(distance)
... 
...     
>>> main()
Enter x coordinates: 4,7
Enter y coordinates: 6,9
4.242640687119285
