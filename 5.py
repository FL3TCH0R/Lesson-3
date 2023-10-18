Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def calculate_order_cost(weight):
...     coffee_price_per_pound=10.50
...     shipping_cost_per_pound=0.86
...     overhead_cost=1.50
...     coffee_cost=weight*coffee_price_per_pound
...     shipping_cost=weight*shipping_cost_per_pound + overhead_cost
...     total_cost=coffee_cost + shipping_cost
...     return total_cost
... 
>>> weight=5
>>> total_cost=calculate_order_cost(weight)
>>> print("The cost for",weight,"pounds of coffee is",total_cost)
The cost for 5 pounds of coffee is 58.3
