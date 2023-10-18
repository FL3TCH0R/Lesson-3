Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Get the time from the user
>>> time = float(input("Enter the time elapsed (in seconds) between the flash and the sound of thunder: "))
Enter the time elapsed (in seconds) between the flash and the sound of thunder: 12
>>> # Constants
>>> speed_of_sound_ft_per_sec = 1100
>>> feet_in_a_mile = 5280
>>> # Calculate the distance in feet
>>> distance_in_feet = time * speed_of_sound_ft_per_sec
>>> # Convert the distance to miles
>>> distance_in_miles = distance_in_feet / feet_in_a_mile
>>> print("The lightning strike is approximately", distance_in_miles, "miles away.")
The lightning strike is approximately 2.5 miles away.
