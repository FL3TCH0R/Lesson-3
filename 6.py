Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     X1,X2=eval(input("Enter X-coordinates:"))
...     Y1,Y2=eval(input("Enter Y-coordinates:"))
...     slope=(Y2-Y1)/(X2-X1)
...     print(slope)
... 
...     
>>> main()
Enter X-coordinates: 4,7
Enter Y-coordinates: 9,12
1.0
