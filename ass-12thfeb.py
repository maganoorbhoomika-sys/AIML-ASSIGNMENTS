# Python program to take name, age, and hobby
# and print a personalized message with age category

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Categorizing age using conditionals
if age < 13:
    category = "a child"
elif age < 20:
    category = "a teenager"
elif age < 60:
    category = "an adult"
else:
    category = "a senior citizen"

# Personalized message
print("\nHello", name + "!")
print("You are", age, "years old and belong to the category:", category)
print("It's great that you enjoy", hobby + "!")