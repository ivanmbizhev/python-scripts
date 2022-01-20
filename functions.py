def multiply(x, y):
    result = x * y
    return result

def is_palindrom(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    #return string[::-1].casefold() == string.casefold()
    return is_palindrom(string)

word = input("Please enter a word check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrom".format(word))
else:
    print("'{}' is not a palindrom".format(word))