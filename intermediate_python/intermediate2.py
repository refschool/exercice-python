""" else in loop """
""" run loop until something is found no need to go further, early exit, else will provide an action if loop 
doesnt exit early like if... else but indentation are different """
for i in range(10):
    print(i)
    if i == 19:
        print("Too big - I'm giving up!")
        break
else:
    print("Completed successfully")

""" apply function to list """
a_list = ["a", "b", "c"]
map_object = map(str.upper, a_list)
new_list = list(map_object)
print(new_list)
print(map_object)

""" list comprehension style  """
new_list = [str.upper(element) for element in a_list]

""" ewuivalent of die in php"""
"""from os import exit"""

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass
# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")