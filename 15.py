Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def approximate_pi(n):
...     approximation=0
...     for i in range(n):
...         term = 4.0 / (2*i + 1) * (-1)**i
...         approximation += term
...     return approximation
... 
>>> n=1000
>>> approximation=approximate_pi(n)
>>> difference=math.pi-approximation
>>> print("Approximation of pi after",n,"terms:",approximation)
Approximation of pi after 1000 terms: 3.140592653839794
>>> print("Actual value of pi:",math.pi)
Actual value of pi: 3.141592653589793
>>> print("Difference:",difference)
Difference: 0.000999999749998981
