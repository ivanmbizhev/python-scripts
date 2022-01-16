empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for number_list in numbers:  # With the loop you can list all of the available lists 
    print(number_list)

    for value in number_list: # with this loop you'll list their contents
        print(value)