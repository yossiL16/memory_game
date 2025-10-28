from copy import deepcopy

from create.create import mix_cards

def Inverted_table(num1 ,num2):

    table = []
    for i in range(num1):
        colu = []
        for j in range(num2):
            colu.append("X")
        table.append(colu)
    return table

def choice(num1,num2):
    choice1 = int(input(f"Choose a place in the line to turn - (0/{num1 -1}) : "))
    choice2 = int(input(f"Choose a place in the column to turn - (0/{num2 -1}) : "))
    return choice1, choice2


def card_selection(table, cards_to_print, num1, num2):

    print(table)
    print()
    print("- - - - - - -")
    print()
    try:
        n1, n2 = choice(num1,num2)

        card1 = cards_to_print[n1][n2]
        table[n1][n2] = card1
        print(table)

        n3,n4 = choice(num1,num2)

        card2 = cards_to_print[n3][n4]
        table[n3][n4] = card2
        print(table)
        # return card1, card2, table, cards_to_print

        if card1 == card2:
            return table
        else:
            table[n1][n2] = "X"
            table[n3][n4] = "X"
            return table

    except:
        print("You exceeded the number")









