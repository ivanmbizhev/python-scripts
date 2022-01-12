age = 31
print("My age is {0} years ".format(age))

print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}"
    .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))


for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))


print()

print(" Pi is approximately {0:<72.54f}". format(22 / 7))

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"

print(data[0:-1:5])

flower = "blue violet" 

print('blue' in flower)