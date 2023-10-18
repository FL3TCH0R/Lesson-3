Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fibonacci(n):
...     if n<=0:
...         return "Input should be a positive integer."
...     elif n==1:
...         return 1
...     elif n==2:
...         return 1
...     else:
...         fib_seq=[1,1]
...         for i in range(2,n):
...             fib_seq.append(fib_seq[i-1]+fib_seq[i-2])
...         return fib_seq[-1]
... 
...     
>>> n = 10
>>> fib_number=fibonacci(n)
>>> print("The",n,"th Fibonacci number is",fib_number)
The 10 th Fibonacci number is 55
