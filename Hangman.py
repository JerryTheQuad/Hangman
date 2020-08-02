import random

print('H A N G M A N')
words = ['аббревиатура', 'солнце', 'карапуз', 'младенец']


def menu():
    while True:
        HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
        random_word = random.choice(words)
        nope = list(random_word)
        player_letters = []
        lives = 8
        random_word_lt = ['-' for w in random_word if w not in player_letters]
        hang_pics = 7
        
        menu_1 = input('Type "play" to play the game, "exit" to quit: ')
        if menu_1 == 'play':
            while True:
                if lives < 8:
                    print(HANGMANPICS[hang_pics - lives])
                    
                print(''.join(random_word_lt))
                player_input = input('Input a letter: ')

                if player_input == random_word:
                    print('You guessed the word!')
                    print('You survived!')
                    break
                elif len(player_input) != 1:
                    print('You should input a single letter\n')

                elif player_input.isalpha() is False or player_input.islower() is False:
                    print('It is not an ASCII lowercase letter\n')

                elif player_input in player_letters:
                    print('You already typed this letter\n')

                elif player_input not in list(random_word):
                    lives -= 1
                    player_letters += player_input
                    if lives > 0:
                        print('No such letter in the word\n')
                    else:
                        print('No such letter in the word')
                        print('You are hanged!\n')
                        print('The correct word was: ' + ''.join(nope) + '\n')
                        print(HANGMANPICS[7] + '\n')
                        break
                elif player_input in list(random_word) and player_input not in player_letters:
                    player_letters += player_input
                    for i in range(0, len(nope)):
                        if nope[i] == player_input:
                            random_word_lt[i] = nope[i]
                    if ''.join(random_word_lt) == random_word:
                        print('You guessed the word!')
                        print('You survived!')
                        break
                    else:
                        print()
                        continue
        elif menu_1 == 'exit':
            break
        else:
            continue


menu()

