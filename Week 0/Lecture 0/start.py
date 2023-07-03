# Methods function with or without parentheses
name = ((input ("What is your name? ")).strip()).title()

# Ways of assigning elements of a list to a variable
first_name, last_name = name.split(" ")
print (last_name)
first_name = name.split(" ")[0]
print (first_name)


print (f"Hello {first_name}")
print ("hi", name) 