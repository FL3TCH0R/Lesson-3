Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def calculate_average():
...     total_numbers=int(input("How many numbers are to be averaged?"))
...     total_sum=0
...     for i in range(total_numbers):
...         number=float(input(f"Enter number {i+1}:"))
...         total_sum+=number
...         average=total_sum/total_numbers
...         print("The average of the numbers is",average)
... 
...         
>>> calculate_average()
How many numbers are to be averaged? 2
Enter number 1: 67
The average of the numbers is 33.5
Enter number 2: 56
The average of the numbers is 61.5
