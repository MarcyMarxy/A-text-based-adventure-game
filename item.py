#Class created but still working on it since I'm finding the way to use the attributes from Room class
from room import Room #This line wont work
class Item():
    def __init__(self,item_name):
        self.name=item_name
        self.content=None
        self.amount=0
    def set_item(self,item_name):
        self.name=item_name
    def get_item(self):
        return self.name

    def set_content(self,item_content):
        self.content=item_content
    def get_content(self):
        return self.content

    def search(self,room_name): #the search method need to look on current_room
        print("self.content")
    def take(self,item_name):
        print("Take a "+item_name)
        self.amount=self.amount-1