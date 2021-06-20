fibonacciOuput = []

def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))
        
upperLimit = int(input("Enter a number:"))

if upperLimit <= 0:
   print("Enter any positive number")
else:
   print("series sequence:")
   for i in range(upperLimit):
       fibonacciOuput.append(Fibonacci(i))

print(fibonacciOuput)
