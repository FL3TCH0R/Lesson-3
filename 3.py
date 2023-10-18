Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Define the molecular weights
>>> hydrogen_weight = 1.007
>>> carbon_weight = 12.011
>>> oxygen_weight = 15.999
>>>  #Get the number of atoms from the user
>>> num_hydrogen = int(input("Enter the number of hydrogen atoms: "))
Enter the number of hydrogen atoms: 24
>>> num_carbon = int(input("Enter the number of carbon atoms: "))
Enter the number of carbon atoms: 14
>>> num_oxygen = int(input("Enter the number of oxygen atoms: "))
Enter the number of oxygen atoms: 8
>>> # Calculate the total weight
>>> total_weight = (hydrogen_weight * num_hydrogen) + (carbon_weight * num_carbon) + (oxygen_weight * num_oxygen)
>>> print("The molecular weight of the carbohydrate is: ", total_weight, "grams per mole")
The molecular weight of the carbohydrate is:  320.314 grams per mole
