import random

def numberguessing_game():
    print("welcome to the Number Guessing Game")
    number_to_guess=random.randint(1,100)
    attempt=0

    while True:
        try:
            user_guess=int(input("enter your guess(1 to 100):"))
            attempt+=1

            if user_guess<1 or user_guess>100:
                print("please guess no betweeen 1 to 100")
            elif user_guess<number_to_guess:
                print("too low,Try again")

            elif user_guess>number_to_guess:
                print("too high ,Try again")
            else:
                print(f"congrats you guessed the number {number_to_guess} in {attempt} attempts")
                break
        except ValueError:
            print("invalid input,Please enter a valid number")

if __name__=="__main__":
    numberguessing_game()

      


        