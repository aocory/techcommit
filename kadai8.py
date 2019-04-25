class Avator:
  def __init__(self,hp,attack):
    self.hp=hp
    self.attack=attack

hero=Avator(30,15)
demon=Avator(40,10)

print("勇者のHP"+str(hero.hp))
print("魔王のHP"+str(demon.hp))

def turn():
  print("勇者の攻撃!魔王は"+str(hero.attack)+"のダメージ")
  demon.hp=int(demon.hp)-int(hero.attack)
  if demon.hp <= 0:
    print("魔王を倒した！")
    return
  print("魔王の攻撃勇者は"+str(demon.attack)+"のダメージ")
  hero.hp=int(hero.hp)-int(demon.attack)
  if hero.hp <= 0:
    print("勇者は倒れた")
    return
  print("勇者のHP"+str(hero.hp))
  print("魔王のHP"+str(demon.hp))


while hero.hp >=0 and demon.hp >=0:
  turn()
