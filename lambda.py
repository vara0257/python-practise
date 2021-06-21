# A lambda function is small anonymous function
# A lambda function can take any number of arguments, but can only have one expression.

# Synatax 
# lambda arguments : expression

# Single argument
x = lambda x: x+10
print(x(5))

# Two arguments
x = lambda a, b : a * b
print(x(5,6))

# Multiple arguments
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Why use of Lambda functions
# Using as anonymous function inside another function

def my_function(n):
    return lambda a: a * n

mydoubler = my_function(2)

print(mydoubler(10))

==============================

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(10))
print(mytripler(10))    
