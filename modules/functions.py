from cgitb import text
from turtle import left, width


def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)

# Call the function

python_food()