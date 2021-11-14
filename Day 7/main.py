# Importing modules
import random
from hangman_words import word_list
from hangman_art import logo, stages

# Chosing random word from word_list
chosen_word = random.choice(word_list)

# Length of random chosen_word
word_length = len(chosen_word)

# Printing Hangman ASCII logo
print(logo)

# Lives of man (stages)
lives = 6

# Creating blanks
display = []
for _ in range(word_length):
    display += "_"

# Printing blanks
# print(display)

# Define end of game for loop
end_of_game = False

# Main algorithm
while not end_of_game:
    guess = input("Guess a letter: ").lower()
        
    if guess in display:
        print(f"You have already guessed {guess}")
    
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word is {chosen_word.upper()}.")
            
    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    print(stages[lives])
   
