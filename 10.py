Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def main():
...     height=eval(input("enter height"))
...     degrees=eval(input("enter angle in degrees"))#inputting angle and height
...     radians=(math.pi/180)*degrees #converting angle to radian
...     length=height/math.sin(radians) #calculating length
...     print(length)#displaying length
... 
...     
>>> main()
enter height 6
enter angle in degrees 45
8.48528137423857
