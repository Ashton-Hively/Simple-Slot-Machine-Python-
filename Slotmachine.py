import random
bet = int(input("Choose bet: "))

while True:
    input()
    slot_symbols = ['$', '7', '1']

    slot1 = random.choice(slot_symbols)
    slot2 = random.choice(slot_symbols)
    slot3 = random.choice(slot_symbols)

    print(slot1, slot2, slot3)

    if slot1 == '$' and slot2 == '$' and slot3 == '$':
        print("You won! ", bet * 2)
    elif slot1 == '7' and slot2 == '7' and slot3 == '7':
    	print("You won! ", bet * 1.5)
    elif slot1 == '1' and slot2 == '1' and slot3 == '1':
    	print("Nuetral ", bet)
    elif slot1 == '7' and slot2 == '$' and slot3 == '$':
    	print("You won! ", bet * 1.25)
    elif slot1 == '$' and slot2 == '$' and slot3 == '7':
    	print("You won! ", bet * 1.25)
    elif slot1 == '1' and slot2 == '$' and slot3 == '$':
    	print("Nuetral ", bet)
    else:
    	print("You lose. ", bet * 0.5)
