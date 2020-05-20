def roll(roll):

    find_d = False
    find_plus = False
    amount = "0"
    sides = "0"
    bonus = "0"

    for letter in roll:
        if letter == 'd' or letter == 'D':
            find_d = True
        elif letter == '+':
            find_plus = True
        elif find_plus:
            bonus += letter
        elif find_d:
            sides += letter
        else:
            amount += letter

    try:
        amount = int(amount)
        sides = int(sides)
        bonus = int(bonus)

        if amount <= 0:
            amount = 1

    except:
        return 0, 0

    return amount, sides, bonus
