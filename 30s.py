#May 11 2020

#This is a program which is game a that requires the user to choose which values of "Die Rolls" to add to their total until it reaches 30, resulting in a win. If the total exceeds 30, it gets reset to 0 and theyy must start again.

from random import seed
from random import randint
import sys
import time

#This function uses the random library to Generate
#random numbers for our die rolls

def die_rolls():

    roll1 = 0
    roll2 = 0

    print('Rollem\' up! (press any key)')

    input()
    
    #A small "animation" for the "die roll"
    for x in range(3):
        sys.stdout.write('| \r')
        time.sleep(0.2)
        sys.stdout.write('/ \r')
        time.sleep(0.2)
        sys.stdout.write('- \r')
        time.sleep(0.2)
        sys.stdout.write('\\ \r')
        time.sleep(0.2)
        sys.stdout.write(' \r')
        time.sleep(0.2)
        sys.stdout.flush()

    seed()
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    roll_tot = roll1 + roll2

    print('\nFirst roll: {}\nSecond roll: {}\nRoll total: {}'.format(roll1, roll2, roll_tot))

    roll_list = [roll1, roll2, roll_tot]
    return roll_list

#This function takes the values from the die roll
#and stores each one into a variable, then asks
#the player to choose one

def choose_val():

    roll_list = die_rolls()
    roll1 = roll_list[0]
    roll2 = roll_list[1]
    roll_tot = roll_list[2]
    
    roll_choice = input('Keep first roll (1), second roll (2), or both (3)? Type "exit" to quit. ')

    #this loop makes sure the player puts in a valid choice.
    #I included a value that automatically sets the total to 30
    #to help with testing and debugging

    while roll_choice not in ['1', '2', '3', 'exit', 'h@x!']:
        print('\nNot a valid choice!')
        roll_choice = input('\nFirst (1), Second (2) or Both (3)? ')
        if roll_choice not in ['1', '2', '3', 'exit', 'h@x!']:
            print('Not a valid choice!')
    
    if roll_choice == '1':
        return roll1
    elif roll_choice == '2':
        return roll2
    elif roll_choice == '3':
        return roll_tot
    elif roll_choice == 'exit':
        return 'exit'
    elif roll_choice == 'h@x!':
        return 'win'

#This function starts the game when called. It
#keeps track of the players total rolls and
#resets, and determines whether they have won

def run_game(pname):

    total = 0
    rolls = 0
    resets = 0

    while total < 30:   
        rolls += 1
        val_to_add = choose_val()

        if val_to_add == 'win':
            print('\nDing! Ding! Ding! Winner, winner, chicken dinner!\n\nTotal rolls: {}\nResets: {}'.format(rolls, resets))
            break
        elif val_to_add == 'exit':
            print('\nQuitter!!!')
            break
        
        total += val_to_add       

        print('\nScore: {}\n'.format(total))

        if total > 30:
            total = 0
            resets += 1
            print('\nAw shucks, you busted! Back to zero for you...\n\nScore: {}'.format(total))
        elif total == 30:

            print('\nDing! Ding! Ding! Winner, winner, chicken dinner!\n\nTotal rolls: {}\nResets: {}'.format(rolls, resets))

            play_again = input('Would you like to play again? (y/n)')

            while play_again not in ['y', 'n']:
                play_again = input('Please type "y" or "n": ')

            if play_again == 'y':
                run_game(pname)
            else:
                print('Seeya next time!')
                break

#These next couple of functions are for the
#tutorial the player has the option of doing
#at the beginning of the game

def roll_animation():
    for x in range(3):
        sys.stdout.write('| \r')
        time.sleep(0.2)
        sys.stdout.write('/ \r')
        time.sleep(0.2)
        sys.stdout.write('- \r')
        time.sleep(0.2)
        sys.stdout.write('\\ \r')
        time.sleep(0.2)
        sys.stdout.write(' \r')
        time.sleep(0.2)
        sys.stdout.flush()


def tut_roll():
    print('Roll\'em up!\n')

    tut_roll_input = input()
    tut_roll_input = str.lower(tut_roll_input)
    
    while tut_roll_input != 'roll':
        tut_roll_input = input('You have to type "roll" here!\n')
    
    roll_animation()


def tutorial():

    print('#~' * 55 + '\n')
    print('Tutorial Time!\n' )
    print('#~' * 55 + '\n\n') 
    time.sleep(0.5)

    print('Your score will start at zero:\n')
    print('Score: 0\n')
    input('Press enter to continue\n')

    print('#~' * 55 + '\n')
    print('Next, you will be asked to roll the die, here you should type "roll"')
    print('Then you will be shown your two rolls and their totoal\n')
    print('#~' * 55 + '\n')
    
    tut_roll()

    print('First roll: 6\n')
    print('Second roll: 6\n')
    print('Roll total: 12\n')    
    time.sleep(0.5)

    print('#~' * 55 + '\n')
    print('You will be asked which value you would like to keep\n')
    print('Here, you should press either the "1", "2" or "3" key\n')
    print('Note that you can also quit by typing "exit\n')
    print('#~' * 55 + '\n')
    time.sleep(0.5)

    print('Keep first roll (1), second roll (2), or both (3)? Type "exit" to quit.\n')

    print('#~' * 55 + '\n')
    print('Press "3" to choose the total of both die to add twelve to your score\n')
    print('#~' * 55 + '\n')
    
    tut_choice_input = input('Type "3"!\n')

    while tut_choice_input != '3':
        tut_choice_input = input('Type "3" here!\n')

    print('#~' * 55 + '\n')
    print('Your score will be updated with your choice:\n')
    print('#~' * 55 + '\n')

    print('Score: 12\n')
    time.sleep(0.5)

    print('#~' * 55 + '\n')
    print('Then we roll again!\n')
    print('#~' * 55 + '\n')

    tut_roll()

    print('First roll: 6\n')
    print('Second roll: 6\n')
    print('Roll total: 12\n')    

    print('Keep first roll (1), second roll (2), or both (3)? Type "exit" to quit. 3\n')

    tut_choice_input = input('Type "3" here for 12 score!')

    while tut_choice_input != '3':
        tut_choice_input = input('Type "3" here!\n')

    print('Score: 24\n')

    tut_roll()

    print('First roll: 6\n')
    print('Second roll: 1\n')
    print('Roll total: 7\n')

    print('#~' * 55 + '\n')
    print('If you choose your first roll here your score will be 30!\n')
    print('Press "1" to choose you first roll and win the game!\n')
    print('#~' * 55 + '\n')

    tut_choice_input = input('Type "1" here for 6 score!')

    while tut_choice_input != '1':
        tut_choice_input = input('Type "1" here!\n')

    print('Score: 30\n')
    print('Ding! Ding! Ding! Winner, winner, chicken dinner!\n')

    print('#~' * 55 + '\n')
    print('Now you can go give it a shot for real!\n')
    print('#~' * 55 + '\n')

#This point marks the start of the program

print('\n\nWelcome to 30s! A game in which the object is to reach a total of exactly 30. You will roll two die, then you will decide whether you want to keep the value from either or both. However, I\'m afraid if your total ever exceeds 30 you will have to start over from zero.\n')

run_tut = input('Would you like to do the short tutorial? (yes or no): ')

while run_tut not in ['yes',  'no']:
    run_tut = input('Please enter "yes" or "no": ')

if run_tut == 'yes':
    tutorial()

player_name = input('If you would do me the honor of revealing your name we can get started! ')

print('\n\nAlright, {} let\'s play 30s!\n\nScore: 0'.format(player_name))

run_game(player_name)
