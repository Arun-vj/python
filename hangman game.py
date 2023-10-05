import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word = ["balloon","apple","mouse"]
chosen_word = random.choice(word)
display = []
word_len = len(chosen_word)
for i in chosen_word:
    display += "_"
print(chosen_word)
print(display)
game_on = True
lives = 6
while game_on:
    guess = input("Guess the word :")
    for i in range(word_len):
        letter = chosen_word[i]
        if guess == letter:
            display[i] = letter
    print(display)
    if guess not in chosen_word:
        lives = lives - 1
        if lives == 0:
            game_on = False
            print("you lose")
    print(stages[lives])
    if "_" in display:
        continue
    else:
        game_on = False
        print("You Lose")






