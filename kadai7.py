print("数字を入力してください")
nn=input()
n=int(nn)
def check(n):
  for p in range(2, n):
    if n % p == 0:
      print(str(n) + '素数ではありません')
      return
  print(str(n) + 'は素数です')
check(n)
