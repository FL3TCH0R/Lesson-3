Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def newtons_method(x, num_iterations):
...     guess = x / 2.0  # Initial guess
...     for _ in range(num_iterations):
...         guess = (guess + x / guess) / 2.0  # Apply Newton's method
...         return guess
... 
...     
>>> x=25
>>> num_iterations=5
>>> estimate = newtons_method(x,num_iterations)
>>> actual=math.sqrt(x)
>>> print(f"Newton's Method estimate for sqrt({x}) after {num_iterations} iterations: {estimate}")
Newton's Method estimate for sqrt(25) after 5 iterations: 7.25
>>> print(f"Actual sqrt({x}): {actual}")
Actual sqrt(25): 5.0
>>> print(f"Difference: {abs(estimate-actual)}")
Difference: 2.25
