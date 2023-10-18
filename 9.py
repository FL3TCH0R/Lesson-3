Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def main():
...     a=34
...     b=32
...     c=40
...     #Defining the sides
...     s=(a+b+c)/2
...     A=math.sqrt(s*(s-a)*(s-b)*(s-c))
...     print(A)
... 
...     
>>> main()
524.3195590477243
