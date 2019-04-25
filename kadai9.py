print ("商品の金額を入力してください")
price=input()
print ("商品の個数を入力してください")
num=input()
tax=1.08
total=int(price)*int(num)*tax
print ("合計金額は"+str(total) + "円です。")
