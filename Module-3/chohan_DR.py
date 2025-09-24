
"""
Cho-Han (modified) — Module 3
Base source: "Cho-Han, by Al Sweigart"
Modifications by Damitrious Rivera:
- House fee changed from 10% to 12%.
- Intro now includes a notice: totals of 2 or 7 award a 10 mon bonus.
- After revealing dice, if total == 2 or 7, output a bonus message and add 10 mon to purse.
Saved as: chohan_DR.py
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print("""Cho-Han (Modified for Module 3)

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

**New rule for this assignment: if the total of the dice is 2 or 7,
you receive a 10 mon bonus added to your purse.**
""")

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('DR: ')  # CHANGED: prompt uses initials and colon.
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('DR: ').upper()  # CHANGED: initials prompt for bet input.
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    total = dice1 + dice2

    # BONUS RULE (NEW): total equal to 2 or 7
    if total in (2, 7):
        print(f'Bonus! The total was {total}. You receive +10 mon.')
        purse += 10

    # Determine if the player won:
    rollIsEven = (total % 2 == 0)
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # Add the pot to player's purse.
        house_fee = int(pot * 0.12)  # CHANGED: 12% fee.
        print('The house collects a', house_fee, 'mon fee.')
        purse = purse - house_fee
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
