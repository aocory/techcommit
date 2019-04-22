# FizzBuzz問題
n=1
while n <101:
  if (n%3==0 and n%5==0):
    print("FizzBuzz")
    n = n+ 1
  elif (n%3==0):
    print("Fizz")
    n = n+ 1
  elif (n%5==0):
    print("Buzz")
    n = n+ 1
  else:
    print(n)
    n = n+ 1
