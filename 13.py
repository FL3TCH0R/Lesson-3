Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sum_numbers():
...     total_numbers=int(input("How many numbers are to be summed?"))
...     total_sum=0
...     for i in range(total_numbers):
...         number=float(input(f"Enter number {i+1}:"))
...         total_sum += number
...         print("The total sum of the numbers is",total_sum)
... 
...         
>>> sum_numbers()
How many numbers are to be summed? 7
Enter number 1: 4
The total sum of the numbers is 4.0
Enter number 2: 6
The total sum of the numbers is 10.0
Enter number 3: 8
The total sum of the numbers is 18.0
Enter number 4: 9
The total sum of the numbers is 27.0
Enter number 5: 10
The total sum of the numbers is 37.0
Enter number 6: 23
The total sum of the numbers is 60.0
Enter number 7: 45
The total sum of the numbers is 105.0
