
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman game using Python strings, loops, conditionals, and user input. This assignment helps you practice game logic, state tracking, and feedback for the player.

## 📝 Tasks

### 🛠️ Word Selection and Game Setup

#### Description
Create a function that selects a random word from a predefined list and initializes the game state.

#### Requirements
Completed program should:

- Use a predefined list of words.
- Select one word at random for each game.
- Initialize a hidden word display using underscores.
- Set the number of attempts or guesses allowed.

### 🛠️ Player Guess Handling

#### Description
Implement the core game loop to accept player guesses, update the displayed word, and track incorrect guesses.

#### Requirements
Completed program should:

- Ask the player to guess a letter.
- Reveal correct letters in the hidden word display.
- Track letters that have already been guessed.
- Decrease remaining attempts for incorrect guesses.
- Prevent repeated penalties for duplicate guesses.

### 🛠️ Win/Lose Conditions and Feedback

#### Description
Add logic to end the game with a win or loss and display appropriate messages.

#### Requirements
Completed program should:

- End the game when the word is fully guessed.
- End the game when the player runs out of attempts.
- Display a clear win message if the player guesses the word.
- Display a clear lose message if attempts are exhausted.
- Show the correct word at the end of the game.
