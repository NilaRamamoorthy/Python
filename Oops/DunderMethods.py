# Section 6: Magic (Dunder) Methods Tasks (36–40)

# 36. Override __add__() in a Vector class to allow vector addition using +
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print("Vector Addition:", v3)

# 37. Override __len__() in a Playlist class to return number of songs.
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

pl = Playlist(["Song A", "Song B", "Song C"])
print("Total songs in playlist:", len(pl))

# 38. Override __getitem__() and __setitem__() in a class that mimics a shopping cart.
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def __getitem__(self, item):
        return self.items.get(item, 0)

    def __setitem__(self, item, quantity):
        self.items[item] = quantity

cart = ShoppingCart()
cart["apple"] = 3
cart["banana"] = 5
print("Apples in cart:", cart["apple"])
print("Bananas in cart:", cart["banana"])

# 39. Override __contains__() in a custom Inventory class to check if item exists.
class Inventory:
    def __init__(self, products):
        self.products = products

    def __contains__(self, item):
        return item in self.products

inv = Inventory(["laptop", "mouse", "keyboard"])
print("mouse" in inv)
print("printer" in inv)

# 40. Create a class Money and implement __eq__, __gt__, __lt__ for comparing amounts.
class Money:
    def __init__(self, amount):
        self.amount = amount

   
