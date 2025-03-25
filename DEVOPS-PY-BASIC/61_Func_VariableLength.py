# When we want to execute the function with any number of parameters, we can use `variable length` arguments.

def addition(*data):
    s = 0
    for i in data:
        s=s+i
    return s;

print("Without 1 arguments: ", addition(10))
print("Without 2 arguments: ", addition(10,20))
print("Without 3 arguments: ", addition(10,20,30))
print("Without 4 arguments: ", addition(10,20,30,40))
print("Without n arguments: ", addition(10,20,30,40,50,60,70,80,90,100))