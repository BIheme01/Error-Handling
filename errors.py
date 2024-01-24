# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program.") # this is a syntax error - need brackets after print function
print ("\n") # this is a syntax error - do not need identation, need brackets after print function 

# Variables declaring the user's age, casting the str to an int, and printing the result

#this is a syntax error, a variable only requires one "=" sign, also indentation is not required
age_str = "24 years old" 

#syntax error - indentation not required before age, change age_str into integer
age = int(age_str.strip("years old")) 

#syntax error - indentation not required, can't concatenate an integer
print(f"I'm {age} years old.")  

# Variables declaring additional years and printing the total years of age

#this is a syntax error - indentation not required, variable should be an integer not string
years_from_now = 3 

total_years = age + years_from_now #this is a syntax error - indentation not required

print(f"The total number of years is: {total_years}") #syntax error, brackets missing, variable should be "total_years"

"""Variable to calculate the total amount of months 
from the total amount of years and printing the result"""
total_months = total_years * 12 #syntax (naming) error, variable name should be "total_years"
                          
#logical error - the total_months variable needs to include 6 more months 
total_months = total_months + 6  

#syntax error, brackets required, cast integer to string for concatenation
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") 
                                                                               

#HINT, 330 months is the correct answer