while True:
    guess = input("Enter an integer: ")
    if guess == "92":
        guess = True
        print("Congratulations, you're correct!")
        break
    elif guess > "92":
        guess = False
        print("Wrong, it's lower")
    elif guess < "92":
        guess = False
        print("Wrong, it's higher")