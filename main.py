from room import Room
from item import Item
from character import Enemy,Character,Friend
from random import choice
#create room
kitchen=Room("Kitchen")
bathroom=Room("Bathroom")
dining_hall=Room("Dining Hall")
outdoor=Room("Outdoor")
bedroom=Room("Bedroom")
garden=Room("Garden")

kitchen.set_description("water and food")
dining_hall.set_description("TV and cellphone")
bathroom.set_description("vacant")
bedroom.set_description("cool")
garden.set_description("a car and a bike")
outdoor.set_description("DANGEROUS")

#kitchen.set_name("Kitchen-Full")

kitchen.link_room(dining_hall,"south")
dining_hall.link_room(kitchen,"north") #cannot add bathroom,"west" here
dining_hall.link_room(bathroom,"west")
bathroom.link_room(dining_hall,"east")
bedroom.link_room(dining_hall,"west")
dining_hall.link_room(bedroom,"east")
garden.link_room(dining_hall,"north")
dining_hall.link_room(garden,"south")
outdoor.link_room(garden,"north")
garden.link_room(outdoor,"south")

#print(dining_hall.linked_rooms["east"])

#create character
angel=Enemy("Angel","Shining in the sky.")
dining_hall.set_character(angel)
angel.set_conversation(choice(["Aaargh!", "Waaagh!", "Braaains!"]))
angel.set_weakness("Hammer")

dave=Character("Dave","A smelly zombie!")
garden.set_character(dave)
dave.set_conversation("May I help you?")

nana=Friend("Nana","A smart human.")
bathroom.set_character(nana)
nana.set_conversation("Hi!^_^")
nana.set_item("make up")

# command=input("> ......") #Which way to go
# if command in ["north","south","west","east"]:
#    current_room=current_room.move(command)
# elif command=="talk":


print("You are in......")
current_room=bedroom
while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        command = input("> What do you want to do......")  # Which way to go
        if isinstance(inhabitant, Enemy):
            if command == "talk":
                inhabitant.say()
                inhabitant.talk()
            else:
                print("> What will you fight with?")
                fight_with = input()
                inhabitant.fight(fight_with)
                result = inhabitant.fight(fight_with)
                if result == False:
                    quit("Game Over...")
                else:
                    current_room.set_character(None)

        elif command == "talk":
            inhabitant.say()
            inhabitant.talk()
            if isinstance(inhabitant, Friend):
                inhabitant.give()
                print(inhabitant.get_item)

        elif command in ["north", "south", "west", "east"]:
            current_room.get_details()
            current_room = current_room.move(command)

        else:
         inhabitant.fight()

    else:
        #current_room.get_details()
        command = input("> Which way to go......")
        current_room = current_room.move(command)
    print("vvvvvvvvvvvvvvvvvvv")





















    # if inhabitant is not None:
    #     inhabitant.describe()
    #     command = input("> What do you want to do......")  # Which way to go
    #     if command == "talk":
    #         inhabitant.say()
    #         inhabitant.talk()
    #         if isinstance(inhabitant,Enemy):
    #             print("> What will you fight with?")
    #             fight_with = input()
    #             inhabitant.fight(fight_with)
    #             result = inhabitant.fight(fight_with)
    #             if result == False:
    #                 quit("Game Over...")
    #             else:
    #                 current_room.set_character(None)
    #         elif isinstance(inhabitant,Friend):
    #             inhabitant.give()
    #             print(inhabitant.get_item)
    #     elif command in ["north", "south", "west", "east"]:
    #         current_room.get_details()
    #         current_room = current_room.move(command)
    #     else:
    #         print("> What will you fight with?")
    #         fight_with = input()
    #         inhabitant.fight(fight_with)
    #         result = inhabitant.fight(fight_with)
    #         if result==False:
    #             quit("Game Over...")
    #         else:
    #             current_room.set_character(None)
    # else:
    #     #current_room.get_details()
    #     command = input("> Which way to go......")
    #     current_room = current_room.move(command)
    # print("vvvvvvvvvvvvvvvvvvv")
