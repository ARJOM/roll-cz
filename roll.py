def roll(roll):

    find_d = False
    amount = "0"
    sides = "0"

    for letter in roll:
        if letter == 'd' or letter == 'D':
            find_d = True
        elif find_d:
            sides += letter
        else:
            amount += letter

    try:
        amount = int(amount)
        sides = int(sides)

        if amount <= 0:
            amount = 1

    except:
        return 0, 0

    return amount, sides
