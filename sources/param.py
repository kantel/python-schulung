x = 10
y = 20

def my_function1(my_x, my_y):
    print(my_x + my_y)
    
my_function1(x, y)

def my_function2():
    global x, y
    print(x + y)

y = 30
my_function2()