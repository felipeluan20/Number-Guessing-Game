from art import art1
import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

picken_number = random.choice(numbers)

print(art1)
print('Welcome to the Number Guessing Game!')
def game(): 
    status = True   
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {picken_number}")
    dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if dif == 'easy':
            attempts = 10
            print(f'You have {attempts} remaining to guess the number.')
    elif dif == 'hard':
            attempts = 5
            print(f'You have {attempts} remaining to guess the number.')
    else:
        print("Please type 'easy' or 'hard' correctely.")


    while status:
        choice = int(input('Make a guess: '))
        if choice != picken_number:
            attempts -= 1
            print(f'You have {attempts} remaining to guess the number.')
        if attempts == 0:
            status = False
            print('You lose.')
        if choice > picken_number:
            print('Too high.')
        elif choice < picken_number:
            print('Too low.')
        else:
            print(f'You got it! The answer was {picken_number}')
            status = False
            
game()

try_again = input('Wanna play again? Type Y or N: ')
if try_again == 'Y':
    print('')
    game()
