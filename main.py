from game.game import card_selection, Inverted_table
from create.create import mix_cards

cards_to_print, num1 ,num2 = mix_cards()
table = Inverted_table(num1 ,num2)
while True:
    table = card_selection(table, cards_to_print, num1, num2)

    x = True
    for i in table:
        if "X" in i:
            x = False
    if x == False:
        continue
    else:
        print("you winn!!!")
        print(table)
        break


