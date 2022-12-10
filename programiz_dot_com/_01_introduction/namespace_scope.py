# https://www.programiz.com/python-programming/namespace

'''Name (also called identifier) is simply a name given to objects. Everything in Python is an object. Name is a way to access the underlying object.

For example, when we do the assignment a = 2, 2 is an object stored in memory and a is the name we associate it with. We can get the address (in RAM) of some object through the built-in function id(). Let's look at how to use it.'''

# Note: You may get different values for the id

# a = 2
# print('id(2) =', id(2))

# print('id(a) =', id(a))

# a = a+1
# print('id(a) =', id(a))

# print('id(3) =', id(3))

# b = 2
# print('id(b) =', id(b))
# print('id(2) =', id(2))

# c = 2
# print('id(c) =', id(c))

#--------------------     . 
# def outer_function():
#     a = 20

#     def inner_function():
#         a = 30
#         print('a =', a)

#     inner_function()
#     print('a =', a)


# a = 10
# outer_function()
# print('a =', a)

# OUTPUT
# a = 30
# a = 20
# a = 10

#--------------------     . 
def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('a1 =', a)

    inner_function()
    print('a2 =', a)


a = 10 #por que ignorou este comando? porque chamou a funcao antes e print
outer_function()
# a = 10 #se estiver aqui, fica 10 mesmo
print('a3 =', a)

#--------------------     . 
# Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)