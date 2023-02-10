## Write a Python program to get the Fibonacci series between 0 to 50

def fibonacci(n):
  if n<0:
    print("Incorrect input")
  elif n==0:
    return 0
  elif n==1 or n==2:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)

print("Fibonacci series between 0 and 50:")
for i in range(10):
  if fibonacci(i) > 50:
        break
  print(fibonacci(i))