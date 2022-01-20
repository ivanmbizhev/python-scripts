from email import parser


def multiply(x, y):
    result = x * y
    return result


answer = multiply(1, 2)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)