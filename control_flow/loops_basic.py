# Loops

# For loop - When we know the number on items we are going to iterate over

# While loop  - When you don't know the exact number of items you're going to iterate over. It run as long as a condition is true and exits when the condition becomes false.


# For loop

# syntax
# 1. Keyword - "for"
# 2. Variable - On each iteration will hold/store the value of an item.
# 3. keyword - "in" - to show membership.
# 4. The object we're performing the loop on.

# Example
# "Hello"

for character in "Hello":
    print(character)  # run on each iteration / loop
    print("Good")


# While

# Syntax
# 1. Keyword "while"
# 2. Condition -- keeps looping if it's true and stops if false.


# Example
# None -- empty or no value
num_of_iteration = 0

while num_of_iteration < 6:
    num_of_iteration = num_of_iteration + 1
    print(num_of_iteration)


# Take Notes of these keywords

# break  - break us out of the closest enclosing loop.

# continue - take us back to the begining of the loop the closest enclosing loop.

# pass - does nothing. We usually use it as a placeholder.


# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number % 2 == 0: 
        # print(number)
        break  # This code will only run if number is even
        # pass
    else:
        print(number) # This will only if number is not even
        # pass
