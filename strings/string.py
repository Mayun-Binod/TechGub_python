# Strings in python are surrounded by either single quotation marks, or double quotation marks.
print("Hello Binod")
a="hello world"
print(a)
# multiline Strings
b="""
Dear Binod,
be better day to day ....
chalenges arrived to you.
thankYou!
"""
print(b)
c='''
Dear Binod,
be better day to day ....
chalenges arrived to you.
thankYou!
'''
print(c)

# Strings are Arrays
d="Hello,binod"
dd=d[2] #return index value
print(dd)

# Looping Through a String
for e in "BinodShrestha":
    print(e) # prints one by one

# To get the length of a string, use the len() function.
f="my name Binod Kumar Shrestha"
ff=len(f) #return length index
print(ff)
print(len(f))

# Check String || Check if NOT
check="I am Binod Stha"
print("Binod" in check) #use "in" membership operator and return boolean
print("binod" not in check) #use "not in" membership operator and return boolean
# Use it in an if-else statement:
checking="check binod in if else statement"
if "check" in checking:
    print("yes it is!")
else:
    print("no it is")

# slicing in string
g=" i am slicing"
gg=g[1:3] #return index value
print(gg)
print(g[:])
print(g[-2:-1])
print(g[-3:-1])
print(g[::])

g1 = "Hello, World!"
print(g1[::-1])
print(g1[::-2])

# modify strings
# Python has a set of built-in methods that you can use on strings.
h="binod SHRESTHA"
print(h.upper())
hh=h.lower() # return lower string
print(hh)

# Remove Whitespace
# This only affects spaces on the outside of the string, not spaces inside the string itself.
# The strip() method in Python removes any leading and trailing whitespace (spaces, tabs, newlines) from a string.
removeWhiteSpace="   hello binod i am removing   "
print(removeWhiteSpace.strip())

replaceString="Binod Shrestha"
print(replaceString.replace("Binod","Saroj"))

# Split String
# In your example, the split() method is used to divide the string into a list based on a specified delimiter. 
i = "Hello, World!"
print(i.split(",")) # This will return a list with two elements: ['Hello', ' World!'].

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
aa = "Hello"
bb = "World"
cc = aa + " " + bb
print(cc)

# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is John, I am {age}"
print(txt)