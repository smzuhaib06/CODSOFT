import random

My_Score = 0
Computer_Score = 0

def game():
    global My_Score,Computer_Score
    print("Game starts....")
    My_choice = input("Choose rock, paper, or scissors: ").lower()
    Computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    print(f"You chose: {My_choice}")
    print(f"Computer chose: {Computer_choice}")
    
    if My_choice == Computer_choice:
        print("It's a tie!")
    elif (My_choice == 'rock' and Computer_choice == 'scissors') or \
         (My_choice == 'scissors' and Computer_choice == 'paper') or \
         (My_choice == 'paper' and Computer_choice == 'rock'):
        print("You Win!")
        My_Score += 1
    else:
        print("You Lose!")
        Computer_Score += 1
    
    print(f"Scores -> You: {My_Score}, Computer: {Computer_Score}")

while True:
    game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
