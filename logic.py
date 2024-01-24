"""
START

Create a programme that works out a person's generation
# Lost Generation — 1883-1900
# Greatest Generation — 1901-1927
# Silent Generation — 1928-1945
# Baby Boomers — 1946-1964
# Generation X — 1965 - 1980
# Millennials — 1981-1996
# Generation Z — 1997-2012
# Generation Alpha — 2013 - present

STOP

"""
#THIS IS PROGRAMME VERSION HAS LOGICAL ERRORS 


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
    
    year = int(input("Please enter the year you were you born, to work out which Generation you belong to: "))
        
    if year >= 2024 or year <1901:
            print("Sorry you have entered an invalid year. Please try again")
            continue
       
    if year >= 2013:
        print(f"You were born in the year {year}. Looks like you're the youngest! You're part of the Generation Alpha ")
        break
    elif year >= 1946:
        print(f"You were born in the year {year}, looks like you're a bouncy Baby Boomer")
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
print(LINE)
print(END)
print(LINE)




# BELOW IS THE CORRECT LOGICAL PROGRAMME 


#while True:
    
#     year = int(input("Please enter the year you were you born, to work out which Generation you belong to: "))
        
#     if year >= 2024 or year <1901:
#             print("Sorry you have entered an invalid year. Please try again")
#             continue
       
#     if year >= 2013:
#         print(f"You were born in the year {year}. Looks like you're the youngest! You're part of the Generation Alpha ")
#         break
#     elif year >= 1997:
#         print(f"You were born in the year {year}, looks like you're a hippy Gen Z")
#         break
#     elif year >= 1981:
#         print(f"You were born in the year {year}, looks like you're a funky Milennial")
#         break
#     elif year >= 1965:
#         print(f"You were born in the year {year}, looks like you're a mature Gen X")
#         break
#     elif year >= 1946:
#         print(f"You were born in the year {year}, looks like you're a bouncy Baby Boomer")
#         break
#     elif year >= 1928:
#         print(f"You were born in the year {year}, looks like you're a part of the legendary Silent Generation")
#         break
#     else:
#         year >= 1901
#         print(f"You were born in the year {year}, wow! you are a true Maverick, the Greatest Generation!!!") 
#         break
        
# print(" ")
# print(LINE)
# print(END)
# print(LINE)