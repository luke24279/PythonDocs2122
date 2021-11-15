# Luke Thompson
# Practice using expression and conditional statements

# An exptression is a problem that must be solved
x = 5 + 5
# 5 + 5 is an "arithmetic" expression

answer = input("What is your name?")

# Funtions/methods must be resolved as expressions as well

# Comparison expressiosn resolve as True or False

print(x == 10)
print(7>=7)
print(7>5)


# A conditional statement runs if its condition is not False
if answer == "Luke":
    print("Hello, Luke! Welcome back!")
    print("This line also prints if your name is Luke.")
elif answer == "Bob":
    print("Hey! You owe me money, BOB!")


else:
    print("Sorry, I only talk to Luke.")
print("This line will print no matter what since it is not in the statement.")

# ^ If checks a condition
# ^ Elif checks a condition if the previous conditions were not True
# You can have as many elifs you want/need
# ^ Else rums if no prior conditions were True

age = input("How old are you?")

age = int(age)

if age >= 10:
    print("You have earned yourself a license.")
elif age == 9:
    print("You need to wait a year till you can get your license.")
else:
    print("You're too young for a license.")
    
