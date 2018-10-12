# Eerste programma
b = 7

def verdubbelB():
   global b
   b = b + b

verdubbelB()

print(b)


# Tweede programma
import time
print(time.strftime(("%H:%M:%S")))

def f(y):
   return 2*y + 1

def g(x):
   return 5 + x + 10

print(f(3)+g(3))