# create your simple Book class in this file
class Item:
    def __init__(self, name="", price=0.0, priority=0, status=""):
        self.name = name
        self.price = price
        self.priority = priority
        self.status = status

    def __str__(self):
        return "{:20s} ${:.2f} ({})".format(self.name, self.price, self.priority)

"""
0. Coffee beans         $  40.00 (1)
1. Watch                $  50.00 (2)
2. Metal detector       $  42.50 (3)

beans = Item("Coffee beans", 40, 1, "c")
print(beans)
"""

