# 【FizzBuzz問題の応用編】基本的な条件分岐の文法確認

n=1
while n <151:
  if (n%3==0):
    print(str(n)+"!")
    n = n+ 1
  elif (str(n)[-1]=="3"):
    print(str(n)+"!")
    n = n+ 1
  else:
    print(n)
    n = n+ 1
