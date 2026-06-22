secret = 7
guess = int(input("Guess a number between 1-10: "))

if guess == secret:
    print("Correct! You win!")
elif guess > secret:
    print("Too high!")
else:
    print("Too low!")