name="Binod"
age=23
price=26.88
age2=age
print("the price is:",price)
print("name:",name)
print(age2)

# identifier
# In Python, identifiers are names used to identify variables, functions, classes, etc. Here are the rules for naming identifiers and variables:

# Rules for Identifiers:
# Start with a letter or underscore (_): The first character must be an alphabet letter (a-z, A-Z) or an underscore (_).
# Example: myVar, _temp, counter1
# Subsequent characters can be letters, digits (0-9), or underscores.
# Example: var123, name_2
# Case-sensitive: myvar and Myvar are different variables.
# Cannot be a keyword: Words like if, else, for, while, True, False, etc. cannot be used as variable names.
# No special characters: Identifiers can't include symbols like @, #, $, %, etc.
# Examples of Valid Identifiers:
my_var = 10
_counter = 5
data123 = "Python"

# Invalid Identifiers:
# 2var = 20      # Starts with a number
# my-var = 15    # Contains a hyphen (-)
# global = 100   # 'global' is a keyword

x = 10
a=type(x)  # Output: <class 'int'>
print(a)
y = 3.14
print(type(y))  # Output: <class 'float'>

z = "Hello"
print(type(z))  # Output: <class 'str'>
