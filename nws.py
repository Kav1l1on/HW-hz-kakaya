import random
import time


class Weapon:
    damage = 0
    durability = 0

    def attack(self, Unit):
        Unit.HP -= self.damage

    def defense(self):
        pass

    def isAlive(self):
        if (self.durability > 0):
            return
        else:
            raise ("Weapon is broke")


class Warrior:
    hp = 100
    Armor = 70
    name = "warrior"

    def isAlive(self):
        if self.HP <=0:
            print(f"Warrior:{self.name} is dead")
            return False
        else:
            return True

    def Isattack(self, warrior):
        if self.weapon.isAlive():
            warrior.HP -= self.weapon.damage
            self.weapon.durability -= 1
            print(f"\n--Warrior:{warrior.name}-- \n has been attacked by \n --warrior:{self.name}--"
                  f"\nNow --{warrior.name}-- has {warrior.HP} HP"
                  f"\nAnd --{self.name}-- has {self.weapon.durability} durability of weapon\n")
        else:
            print("\nWeapon is broken\n")
            return False


class Rider(Warrior):
    def __init__(self, name):
        super().__init__()
        self.HP = 70
        self.Armor = 100
        self.name = name
        self.weapon = Sword()


class Weapon:
    damage = 0
    durability = 15
    def isAlive(self):
       if(self.durability<=0):
          return False
       else:
          return True


class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 20
        self.durability = 5


class Gopher(Warrior,):
    def __init__(self, name):
        super().__init__()
        self.Armor = 40
        self.HP = 120
        self.name = name
        self.weapon = Sword()


class Bow(Weapon):
   def __init__(self):
      super().__init__()
      self.damage = 90
      self.durability = 1


class Bowman(Warrior):
    def __init__(self, name):
        super().__init__()
        self.HP = 70
        self.Armor = 100
        self.name = name
        self.weapon = Bow()


class Stick(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 90
        self.durability = 1


class Stickman(Warrior):
    def __init__(self, name):
        super().__init__()
        self.HP = 70
        self.Armor = 100
        self.name = name
        self.weapon = Stick()


army1 = []
for i in range(0, 3):
    name = input("Enter the name for warrior: ")
    army1.append(Rider(name))
for rider in army1:
    print(f"{rider.name}: HP={rider.HP}, Armor={rider.Armor}, Weapon={rider.weapon.__class__.__name__}")

for Stickman in army1:
    print(f"{Stickman.name}: HP={Stickman.HP}, Armor={Stickman.Armor}, Weapon={Stickman.weapon.__class__.__name__}")

for Bowman in army1:
    print(f"{Bowman.name}: HP={Bowman.HP}, Armor={Bowman.Armor}, Weapon={Bowman.weapon.__class__.__name__}")

army2 = []
for i in range(0, 3):
    name = input("Enter the name for warrior: ")
    army2.append(Rider(name))
for rider in army2:
    print(f"{rider.name}: HP={rider.HP}, Armor={rider.Armor}, Weapon={rider.weapon.__class__.__name__}")

for Stickman in army2:
    print(f"{Stickman.name}: HP={Stickman.HP}, Armor={Stickman.Armor}, Weapon={Stickman.weapon.__class__.__name__}")

for Bowman in army2:
    print(f"{Bowman.name}: HP={Bowman.HP}, Armor={Bowman.Armor}, Weapon={Bowman.weapon.__class__.__name__}")

counf_fight = 0
while(army2 and army1):
    choice = random.randint(1,2)
    counf_fight += 1
    print(f"Fight : {counf_fight}")
    if choice == 1:

        warrior_from_army1 = random.randint(0, len(army1)-1)
        warrior_from_army2 = random.randint(0, len(army2)-1)

        if army1[warrior_from_army1].Isattack(army2[warrior_from_army2]):
            army1.pop(warrior_from_army1)
        else:
            if army2[warrior_from_army2].isAlive():
                pass
            else:
                army2.pop(warrior_from_army2)
    if choice == 2:
        warrior_from_army1 = random.randint(0, len(army1) - 1)
        warrior_from_army2 = random.randint(0, len(army2) - 1)

        if army2[warrior_from_army2].Isattack(army1[warrior_from_army1]):
            army2.pop(warrior_from_army2)
        else:
            if army1[warrior_from_army1].isAlive():
                pass
            else:
                army1.pop(warrior_from_army1)

    time.sleep(3)




