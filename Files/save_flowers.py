plants_filename = "flowers_write.txt"

with open(plants_filename, "w") as plants:
    for plant in data:
        plants.write(plant)

print(data)