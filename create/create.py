import random


def create_size_table():
    while True:
        try:
            size1 = int(input("What is the size of the row?: "))
            size2 = int(input("What is the size of the column?: "))
            if (size1 * size2) % 2 != 0 or size1 <= 1 or size2 <= 1:
                print("The board needs to be greater than 2 and even.")
                continue
            return size1, size2
        except:
            print("please enter only numbers")


def create_cards():
    size_tuple = create_size_table()
    num1, num2 = size_tuple[0], size_tuple[1]
    cards = []
    for i in range(num1 * num2 // 2):
        cards.append(str(i + 1))
        cards.append(str(i + 1))
    return cards

def create_table_game():
    cards = create_cards()
    for i in range(len(cards) // 2):
        row = []
        for j in range(len(cards) // 2):
            colu = []











