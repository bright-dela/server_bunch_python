# Error Handling

# The try block
# let you test a block of code for errors.

# The except block
# let us handle the error.

# The else block
# let us run code when there is no error.

# The finally block
# let us run code, regardless of the result of the try and except blocks.


while True:
    try:
        fav_number = int(input("Please enter your favorite number: "))
        if type(fav_number) == int:
            pass
    except ValueError:
        print("\nError: Please enter a numeric value")
    # except TypeError:
    #     print("Error: This is a type error")
    else:
        print(10 + fav_number)
        break
    finally:
        print("\nI always run regardless\n")
