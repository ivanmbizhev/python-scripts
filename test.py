from hashlib import new


list = ["a", "b", "c", "d"]

for letter in list:
    for index in range(len(letter)):
        if letter[index] == "a":
            del list[index]
        print(list[index])

new_list = list
new_list.append("a")
print(new_list)

if "a" in new_list:
    print("Okay")
else:
    print("Not okay")