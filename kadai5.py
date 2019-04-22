# やや複雑な条件分岐の文法確認

n=1
while n <151:
  if (n <100):
    if (n%3==0):
      print(format(n, '0>2')+"!")
      n = n+ 1
    elif (str(n)[-1]=="3"):
      print(format(n, '0>2')+"!")
      n = n+ 1
    else:
      print(format(n, '0>3'))
      n = n+ 1
  else:
    print(n)
    n = n+ 1
