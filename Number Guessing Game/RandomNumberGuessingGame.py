#Random number guesser

import random

low = 1
high = 100
T = random.randint(low, high)
turn = 3

print('Python Number Guessing Game!')
print(f'Select a number between {low} and {high}')

for i in range(0, turn):
        G = input("Enter a guess: ")
        if G.isdigit() and (low < int(G) < high) :
            G = int(G)
            if G == T:
                print("Your guess was correct!")
                break
            elif G > T:
                print('Go lower')
            elif G < T:
                print('Go higher')
        else:
            print(f'Please enter a number between {low} and {high}')

print('Sorry! You ran out of turns!')
print(f'The number was {T}!')