choice = "-"
while choice != "0":
    if choice in set("12345"):
    #if choice in {"1", "2", "3", "4", "5"}:
        print(f"Your choice {choice}")
    else:
        print("Please choose your opiton from the list below: ")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo train")
        print("4:\tEat you piglet!")
        print("5:\tGot to bed")
        print("0:\tExit")

    choice = input()