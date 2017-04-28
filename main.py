"""
Name:
Date:
Brief Project Description:
GitHub URL:
Testing
"""

from kivy.app import App
from kivy.lang import Builder
from item import Item
from itemlist import ItemList
from kivy.uix.button import Button

class ShoppingListApp(App):
    def on_start(self): # this will do initialization
        print("on_start is called.")
        # file opening
        myfile = open("items.csv", "r")
        itemlists = myfile.readlines()
        print(itemlists)
        myfile.close()
        #....linking
        temp_button = Button(text="Testing one")
        temp_button.bind(on_release=self.press)
        self.root.ids.entriesBox.add_widget(temp_button)

        temp_button = Button(text="Testing two")
        temp_button.bind(on_release=self.press)
        self.root.ids.entriesBox.add_widget(temp_button)

    def press(self, instance):
        pass

    def build(self):
        self.title = "Shopping list application"
        self.root = Builder.load_file("app.kv")
        return self.root
