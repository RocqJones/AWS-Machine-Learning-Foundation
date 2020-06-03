from shirt import Shirt

new_shirt = Shirt('Red', 'M', 'short sleeve', 50)

print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)

# change price method
new_shirt.change_price(32)
print(new_shirt.price)

# discount method
print(new_shirt.discount(0.2))

tshirt_collection = []

shirt_one = Shirt('red', 'S', 'short-sleeve', 15)
short_two = Shirt('blue', 'M', 'long-sleeve', 35)
short_three = Shirt('yellow', 'L', 'short-sleeve', 20)

tshirt_collection.append(shirt_one)
tshirt_collection.append(short_two)
tshirt_collection.append(short_three)

for i in range(len(tshirt_collection)):
    print(tshirt_collection[i].color)