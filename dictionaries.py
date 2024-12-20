                




world_capitals = {
"Italy": "Rome",
"Netherlands": "Amsterdam",
"Romania": "Bucharest",
"Spain": "Madrid",
"Russia": "Moscow"}

#accesing the key_value
city = (world_capitals["Italy"])
print(city)

#updating the value

world_capitals["Italy"] = "Teo"
print(world_capitals)

#adding the values

world_capitals["India"] = "New Delhi"
print(world_capitals)

#deleting a key

del world_capitals["Italy"]
print(world_capitals)

#checking for membership

if "Italy" in world_capitals:
    print (world_capitals["Italy"])

#iterating over keys
for key in world_capitals.keys():
    print(world_capitals[key])

#iterating over values
for value in world_capitals.values():
    print(value)


print(len (world_capitals))

