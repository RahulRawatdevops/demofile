import random
def guess_the_number():
  print("Welcome to the number guessing game!")

  play_again = True
  while play_again:
    
  secret_number = random.randint(1, 100)
  attempts = 0
  max_attempts = 7
  hint_after_attempt = 4

while attempt < max_attempts:
  user_guess = int(input("Guess the number (between 1 and 100: "))
  attempts += 1

while True:
  user_guess = int(input("Guess the number (between 1 and 100): "))
  attempts = 0

if user_guess == secret_number:
  print(f"Congratulations! You guessed the number in {attempts} attempts.")
  break
elif user_guess < secret_number:
  print("Too low! Try again.")
else:
  print("Too high! Try again.")

if attempts == hint_after_attempt:
  print(f"Hint: The number is between {secret_number -10} and {secret_number + 10}.)

if attempts == max_attempts:
 print(f"sorry, you have reached the maximum attempts. The correct numbaer was {secret number}."

play_again_input = input("Do you want to play again? (yes/no): " ).lower()
play_again == play_again_input == 'yes'

if __name__ == "__main__":
  guess_the_number()
