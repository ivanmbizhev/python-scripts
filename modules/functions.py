def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)

def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text

#with open("centred", mode='w') as centered_file:

# Call the function
print(centre_text("spam and eggs"))
print(centre_text("spam, spam and eggs"))
print(centre_text(12))
print(centre_text("spam, spam, spam and spam"))

print(centre_text("first", "second", 3, 4, "spam", sep=':'))

print("=" + str(12*3))
print(sorted(["b", "d", "c", "a"]))
