# Luke Thompson
# Assignment examples

# You can assign "values" to "variables"
#by using an equals (right side goes into left side)
x=5

# When Python reads a variable name, it replaces it
# with the variable's stored value
y = x + 5

# There are four different primitive datatypes
# Integers: any whole number, positive or negative
age = 16

# Float: any number with a decimal, positive or negative
grade = 98.6

# String: a string of human-readable characters
name = "Chris"
# numbers in a string are not numbers, they are letters
favoriteNumber = "6\'9"

# Boolean: True or false
# True is 1 in binary, false is 0. True is any value that is not false or empty. True is HIGH voltage, false is LOW
isSmart = True

# You can output to the console by using "print"
print(age)
print(grade)
print(name)
print(isSmart)
print(favoriteNumber)

# You can concatonate similar values together
print("My name is " + name)
# You can use functions to convert datatypes
print("and my age is " + str(age))
# Dont forget! If you want to convert a value permanently
# You must assign the converted value to a variable
age =  str(age)

# You can convert back and forth with int(), str(), bool(), and float()
print(int(age))
print(float(age))
print(bool(age))
