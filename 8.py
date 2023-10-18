Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     year=eval(input("Enter a four digit year:"))
...     C=year//100
...     epact=(8+(C//4)-C+((8*C+13)//25)+11*(year%19))%30
...     print(epact)
... 
...     
>>> main()
Enter a four digit year: 2009
3
