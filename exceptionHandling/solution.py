# Write a Python program that takes two numbers as input and divides the first number by the second number. Use exception handling to manage division by zero.
try:
    number1=int(input("enter the first number:"))
    number2=int(input("enter the second number:"))
    result=number1/number2
    print(f"the result is {result}")

except ZeroDivisionError:
    print("zero is not allowed it gives error")

except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print("Division completed successfully, no errors occurred.")
finally:
    print("i am always ready to run because i am finally")




