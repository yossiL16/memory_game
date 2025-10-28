from create.create import mix_cards

def Inverted_table():
    cards_to_print, num1, num2 = mix_cards()

    table = []
    for i in range(num1):
        colu = []
        for j in range(num2):
            colu.append("X")
        table.append(colu)
    return table, cards_to_print, num1, num2

def card_selection():
    table, cards_to_print, num1, num2 = Inverted_table()
    print(table)
    print(cards_to_print)