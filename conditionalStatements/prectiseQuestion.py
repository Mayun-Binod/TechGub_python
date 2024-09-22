# Check if a number is positive, negative, or zero by user.
# number=int(input("enter the number:"))
# if number>0:
#     print("the number is positive")
# elif number<0:
#     print("the number is negative")
# else:
#     print("sorry the number is zero enter by user")

# Check if a number is even or odd by user.
# number1=int(input("enter the even or odd number:"))
# if number1%2==0:
#     print("the number is even")
# else:
#     print("the number is odd")

# Find the largest of two numbers.
# numb1=float(input("enter the number1 largest:"))
# numb2=float(input("enter the largest number2:"))
# if numb1>numb2:
#     print("the numb1 is largest")
# elif numb2>numb1:
#     print("the numb2 is largest")
# else:
#     print("not largest")

# Write a program to check if a number is divisible by 5 and 11 or not.
# number3=55
# if number3%5==0 and number3%11==0:
#     print("yes it is divisible by 5 and 11")
# else:
#     print("not divisible")

# Check if a character is a vowel or consonant.
character = input("Enter a character: ").lower()
if character in 'aeiou':
    print("It is a vowel")
else:
    print("It is a consonant")

# Find the largest among three numbers:
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("The largest number is:", largest)

# Check if a character is an alphabet:

ch = input("Enter a character: ")

if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print(ch, "is an alphabet.")
else:
    print(ch, "is not an alphabet.")

# Check if a number is within the range of 1 to 100:

number66 = float(input("Enter a number: "))

if number66 >= 1 and number66 <= 100:
    print(number66, "is within the range of 1 to 100.")
else:
    print(number66, "is out of range.")

# Check if a number is a multiple of 3 or 7:
numbers = int(input("Enter a number: "))

if numbers % 3 == 0:
    print(numbers, "is a multiple of 3.")
elif numbers % 7 == 0:
    print(numbers, "is a multiple of 7.")
else:
    print(numbers, "is not a multiple of 3 or 7.")
