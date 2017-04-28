"""
(incomplete) Tests for Book class
"""
from item import Item

# test empty book (defaults)
item = Item()
print(item)
assert item.name == ""
assert item.price == 0.0
assert item.priority == 0

# test initial-value book
item2 = Item("Coffee beans", 40, 1, 'r')
print(item2)
# test mark_completed()