from clear import clear
import random
import hangman_art
import hangman_words
# alternatively, write
#from hangman_words import word_list
# then word_list can be used normally without the prefix

# Variables
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
guess_list = []
end_of_game = False
lives = 6
print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
          
    print(hangman_art.logo)
  
    if guess in guess_list:
      print(f"\nYou have already guessed '{guess.upper()}'. Please try again.")
  
    #Check if user is wrong.
    if guess not in chosen_word:
      if guess not in guess_list:
        lives -= 1
        if lives > 0:
          print(f"\n'{guess.upper()}' is not in the word, please try again.")
      
    if lives == 0:
        end_of_game = True
        print("\nYou lose! :( ")
        print(f"The word was {chosen_word}")
      
    #Check if user has got all letters.
    elif "_" not in display:
        end_of_game = True
        print("\nYou win! :) ")

    print(hangman_art.stages[lives])

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n")
      
    guess_list.append(guess)
