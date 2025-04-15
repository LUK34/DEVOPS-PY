#Error Handling:  error handling allows you to gracefully catch and manage exceptions (runtime errors) so your program doesn’t crash unexpectedly.
try:
    num=int(input("Enter a number:"))
    result=10/num
except ZeroDivisionError:
    print("Cannot divide by 0!")
except ValueError:
    print("Not a number. Please enter a valid number!")