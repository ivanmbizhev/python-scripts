import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open('recepies', writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta
    

    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    # recipes["soup"].append("croutons")


    for snack in recipes:
        print(snack, recipes[snack])