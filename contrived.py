numbers = [1, 45, 31, 16, 60]

for number in numbers:
    if number %8 == 0:
        print("The numbers are unnacceptable")
        break
else:
    print("All those numbers are fine. ")