class Avatar:
    def __init__(self, name, hair, initial_gold):
        self.name = name
        self.hair_color = hair
        self.gold = initial_gold
        self.buried_gold = 0.0

    def find_gold(self, amount):
        '''Add found gold to gold on hand'''
        self.gold += amount

    def bury_gold(self, amount):
        '''Bury some of the avatars gold'''
        if amount <= self.gold:
            self.gold -= amount
            self.buried_gold += amount
        else:
            print("You don't have that much gold")

    def sprinkled_with_fairy_dust(self):
        self.gold *= 1.1

# __STR__ METHOD:
# Also create a __str__ method which returns information about the Avatar,
# including amount of gold in bag, and amount of gold in the ground.
# You can decide on the format to use in printing out these things, just
# be sure to print out at least the name of the Avatar, and the amount
# of gold carried (in bag) and the amount of gold buried (in the ground).

    def __str__(self):
        return f"Here is {self.name}, with {self.hair_color} hair, {self.gold} gold, and a stash of {self.buried_gold} gold."


# ==>  Wild Girl should have 5.75 gold in bag, and 2.5 gold buried.
# ==>  Mad Max should have 28.3195 gold in bag, and 21.5 gold buried.
wildgirl = Avatar("Wild Girl", "purple", 5.5)
print(wildgirl)
wildgirl.find_gold(2.0)
print(wildgirl)
wildgirl.sprinkled_with_fairy_dust()
print(wildgirl)
wildgirl.bury_gold(2.5)
print("==============================")
print("check totals here:")
print(wildgirl)
print("==============================")
madmax = Avatar("Mad Max", "black", 6.5)
print(madmax)
madmax.find_gold(25.0)
print(madmax)
madmax.bury_gold(2.0)
madmax.sprinkled_with_fairy_dust()
madmax.bury_gold(4.5)
madmax.sprinkled_with_fairy_dust()
madmax.find_gold(10.0)
madmax.bury_gold(15.0)
madmax.sprinkled_with_fairy_dust()
print("==============================")
print("check totals here:")
print(madmax)
print("==============================")
