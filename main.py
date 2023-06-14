import random

options = ['rock','paper','scissor']



def main():
    
    user_wins = 0
    computer_wins = 0
    
    while True:
        user_input = input("Type rock/paper/scissor or Q for quit the game and check your score: ").lower()
        
        if user_input == 'q':
            break
        if user_input not in options:
            continue
        
        random_number = random.randint(0,2)
        # rock:0
        # paper:1
        # scissor:2
        computer_pick = options[random_number]
        print('Computer picked', computer_pick, '.')
        
        if user_input == 'rock' and computer_pick == 'scissor':
            print('You win the game!')
            user_wins += 1
        
        elif user_input == 'paper' and computer_pick == 'rock':
            print('You Win the game!')
            user_wins+=1
            
        elif user_input == 'scissor' and computer_pick == 'paper':
             print('You win the game!')
             user_wins += 1
             
        else:
            print('Sorry,You Lose the game!')
            computer_wins +=1
            
    print("You're Score", user_wins,'.' )
    print("Computer Score", computer_wins, ".")
    print('Game End!')

if __name__ == "__main__":
    main()
