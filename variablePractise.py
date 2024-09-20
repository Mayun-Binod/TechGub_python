# Creates three variables: name, age, and is_student.
# Assign the following values to them:
# name: A string representing your name.
# age: An integer representing your age.
# is_student: A boolean indicating whether you are a student or not.
# Print each variable along with its type using the type() function.
name="Binod"
age=23
is_student=True
print(type(name))
print(type(age))
print(type(is_student))

# Write a Python program that:
# Accepts the user's name (string), age (integer), and a list of their favorite hobbies.
# Store these values in appropriate variables: name1, age1, and hobbies.
# Convert the age to a float and store it in a new variable age_in_float.
# Create a dictionary called user_info that stores the user's name, age, and hobbies as key-value pairs.
# Print the dictionary, and for each key, print the type of its value using the type() function.

name1=input("enter the name:")
age=int(input("please add your age:"))
hobbies_input = input("Enter your favorite hobbies: ")
hobbies = [hobby.strip() for hobby in hobbies_input.split(",")]
age_in_float=float(age)
print(age_in_float)

user_info={
    "name":"Saroj",
    "age":26,
    "hobbies":["gaming","travelling","watching"]
}
print(user_info)
print(type(user_info["age"]),type(user_info["name"]),type(user_info["hobbies"]))