# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #syntax error - should have quotation marks
animal_type = "cub"
number_of_teeth = 16

#syntax and logical error - variables in wrong order and 'f' missing from f-string
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" 
print(full_spec) # syntax error - brackets missing