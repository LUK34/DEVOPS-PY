# write a script using python to test the login module.

"""
assume:
facebook page => login page
username => 'admin'
password => 'admin123'

"""

username = input("Enter the username: ")
password = input("Enter the password: ")
if username == 'admin' and password =='admin123':
    print("Welcome to Facebook !!")
else:
    print("Account is not found with given details")




