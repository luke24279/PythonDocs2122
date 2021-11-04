# import the basics module to use its code

import basics

# Make a new application object from the basics module

app = basics.newProgram()

# Use a method that belongs to our new application object

app.print("yo momma ")

# Print a property of our new application object

app.print( app.debugging )

# This line won't print if app.debugging is False

app.debug("Hello")

# We'll enab;e debugging for the application

app.debugging = True
app.debug("Now it works!")

# Import a default Python module
import random

# Use a method from the random module
randomNumber = random.randint(1, 10)

app.print(randomNumber)
