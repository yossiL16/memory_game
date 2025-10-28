import random
from copy import deepcopy
from itertools import count


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

    if num1 % 2 != 0 or num2 % 2 != 0:
        num1 += 1
    range_row = (num1 + num2) // 2
    range_colu = (num1 + num2) // 4

    cards = []
    counter = 1

    for i in range(range_row):
        row = []
        for j in range(range_colu):
            row.append(str(counter))
            row.append(str(counter))
            counter += 1
        cards.append(row)
    return cards, num1, num2

def nix_cards():
    cards, num1, num2 = create_cards()
    cards_mix = deepcopy(cards)

    for i in range(1500):
        random_number_row_1 = random.randrange(0,num1)
        random_number_colu_1= random.randrange(0 ,num2)

        random_number_row_2 = random.randrange(0, num1)
        random_number_colu_2 = random.randrange(0, num2)

        cards_mix[random_number_row_1][random_number_colu_1],cards_mix[random_number_row_2][random_number_colu_2] = cards_mix[random_number_row_2][random_number_colu_2],cards_mix[random_number_row_1][random_number_colu_1]
        return cards, cards_mix

