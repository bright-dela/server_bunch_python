# comparison operators

# == - equality operator
# <  - less-than ooperator
# >  - greater-than operator
# <= - less-than or equal-to operator
# >= - grater-than or equal-to operator
# != - not eqaul to


# True or False

print( 9 < 2 )
print( 10 != 100)

# print( "abc" == "Abc") # this is case-sensitive


# IF-ELSE STATEMENTS

# Score Grading Calculator

# 1. if score greater than 80, then grade A
# 2. if score greater than 70, then grade B
# 3. if score greater than 60, then grade C
# 4. if score 60 and below, then print "Pass"

# Note down
# Keyword are "IF", "ELIF", "ELSE"
# "IF" - mandatory

score = int(input("Please enter your score: ")) 
# the input function always returns a string.
# score = int(score)
# print(type(score))

# if-else statement runs from top to bottom and only run a block of code if the condition is true.

if score >= 80:        # any value greater or equal to 80,
    print("Grade A")

elif score >= 70:      # 79 and 70 inclusive
    print("Grade B")

elif score >= 60:      # 69 - 60 inclusive
    print("Grade C")

else:                  # 59 and below
    print("Pass")

# print("End of our score grading calculator")






number = 100

if number >= 90: 
    print("Yes, I'm greater than 90.")

if number >= 70:
    print("Yes, I'm greater than 70.")

if number >= 50:
    print("Yes, I'm greater than 50.")




