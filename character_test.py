from random import choice
from character import Character
from character import Enemy
dave=Character("Dave","A smelly zombie!")
dave.describe()
dave.talk()
dave.say()
dave.fight("sword")
dave.set_conversation("May I help you?")
dave.talk()
#dave.set_conversation(choice(["Aaargh!", "Waaagh!", "Braaains!"]))

angel=Enemy("Angel","Shining in the sky.")
angel.describe()
angel.set_conversation(choice(["Aaargh!", "Waaagh!", "Braaains!"]))
angel.talk()

angel.set_weakness("Hammer")
print(angel.get_weakness())

print("What will you fight with?")
fight_with = input()
angel.fight(fight_with)