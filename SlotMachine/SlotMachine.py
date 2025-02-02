# Python Slot Machine
import random
import time


def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐','❌']
    results = []

    return [random.choice(symbols) for symbol in range(3) ]

#    for symbol in range(3):
#        results.append(random.choice(symbols))
#    return results

def print_row(row):
    print('*************')
    print(" | ".join(row))
    print('*************')

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row [0] == '🍒' or row[0] == '🍋':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '⭐':
            return bet * 10
        elif row[0] == '🔔':
            return bet * 7
        elif row[0] == '❌':
            return 0
    elif check_two(row, bet):
        return bet * 2
    return 0

def check_two(row, bet):
        if (row[0] == row[1] != row[2]) or (row[0] == row[2] != row[1]) or (row[1] == row[2] != row[0]):
            if row[0] == '🍒' or row[0] == '🍋' or row[0] == '🍉':
                if row[1] == '🍒' or row[1] == '🍋' or row[1] == '🍉':
                    return bet * 2
            if row[1] == '🍒' or row[1] == '🍋' or row[1] == '🍉':
                if row[2] == '🍒' or row[2] == '🍋' or row[2] == '🍉':
                    return bet * 2
            if row[0] == '🍒' or row[0] == '🍋' or row[0] == '🍉':
                if row[2] == '🍒' or row[2] == '🍋' or row[2] == '🍉':
                    return bet * 2
            # elif row[0] == '🔔' or row[0] == '⭐' or row[0] == '❌':
            #     return 0
            # elif row[1] == '🔔' or row[1] == '⭐' or row[1] == '❌':
            #     return 0
        return 0


def main():
    balance = 100

    print('*******************')
    print('Welcome to Slot Machine X!')
    print('Symbols: 🍒 🍉 🍋 🔔 ⭐')

    while balance > 0:
        print(f'Current Balance is ${balance}')

        bet = input('Place your bet amount: ')

        if not bet.isdigit():
            print('Please enter a valid number.' )
            continue

        bet = int(bet)

        if bet > balance:
            print('Insufficient Funds.')
            continue

        if bet <= 0:
            print('Bet must be greater than 0')
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        time.sleep(0.4)
        print('Still Spinning...\n')
        time.sleep(0.6)
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f'You won ${payout}')
        else:
            print('Sorry you lost this round!')

        balance += payout

        play_again = input('Do you want to play again ? (Y/N) : ').upper()

        if play_again != 'Y':
            break

    print('*************************')
    print('Game Over!')
    print(f'Your final balance is ${balance}')
    print('*************************')

if __name__ == '__main__':
    main()