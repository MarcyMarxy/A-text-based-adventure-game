class Room():
    def __init__(self,room_name):
        self.name=room_name
        self.description=None
        self.linked_rooms = {}
        self.character=None

    def set_description(self,room_description):
        self.description=room_description
    def get_description(self):
        return self.description
    def describe(self):
        print(self.description)
    def set_name(self,room_name1):
        self.name=room_name1
    def get_name(self):
        return self.name
    #def __init__(self,roomname):   放initialise里，先创建一堆没有值的东西
       # self.linked_rooms={}
    def link_room(self,room_to_link,direction):
        self.linked_rooms[direction]=room_to_link
        #print(self.name + " linked rooms " + repr(self.linked_rooms))
    def get_details(self):
        print(self.get_name())
        self.describe()
        print("-----------------------")
        for direction in self.linked_rooms:
            room=self.linked_rooms[direction]
            print("The "+ room.get_name()+" is "+direction)
        #print("vvvvvvvvvvvvvvvvvvvvvvv")
    def move(self,direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("Yoou can't go this way")
            return self

    def set_character(self,who):
        self.character=who
    def get_character(self):
        return self.character

    #def set_item