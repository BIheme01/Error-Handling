#THIS IS THE PROGRAMME OF LOGICAL ERRORS 


LINE = "-"*100
welcome = "Welcome to my programme of logical errors. Let's begin :)"
END = "That's the end of the programme. Thank you for visiting. I hope you come back soon :)"

print(LINE)
print(" ")
print(welcome)
print(" ")
print(LINE)
print(" ")

while True:
    
    #compilation error, variable should only have one "=" sign and be cast to integer
    year == (input("Please enter the year you were you born, to work out which Generation you belong to: "))
    print year #compilation error - print should be followed by brackets    
    
    if year >= 2024 or year <1901:
            print("Sorry you have entered an invalid year. Please try again")
            continue   
    if year >= 1946: 
        print(f"You were born in the year {year}, looks like you're a bouncy Baby Boomer")
        break
    elif year >= 2013: #logical error - the year 1946 is the first statment, years greater than 2013 would be classed as Baby Boomers
        print(f"You were born in the year {year}. Looks like you're the youngest! You're part of the Generation Alpha ")
        break
    elif year >= 1981:
        print(f"You were born in the year {year}, looks like you're a funky Milennial")
        break
    elif year >= 1928:
        print(f"You were born in the year {year}, looks like you're a part of the legendary Silent Generation")
        break
    elif year >= 1965:
        print(f"You were born in the year {year}, looks like you're a mature Gen X")
        break
    elif year >= 1997:
        print(f"You were born in the year {year}, looks like you're a hippy Gen Z")
        break
    else:
        year >= 1901
        print(f"You were born in the year {year}, wow! you are a true Maverick, the Greatest Generation!!!") 
        break
        
print(" ")
RuntimeError = year/0 #this is ZeroDivisonError (a runtime error), you cannot divide by zero
print(RuntimeError)
print(LINE)
print(END)
print(LINE)