import random
import time

rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """

paper = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """

scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """



user_input = input("Do you want to play? Y/N? ")

if user_input.lower() == "y":
    while True:
        user_choice = int(input("0 for Rock, 1 for Paper, and 2 for Scissors: "))
        if user_choice == 0:
            print(rock)
            print("I choose rock!")
        elif user_choice == 1:
            print(paper)
            print("I choose paper!")
        
        elif user_choice == 2:
                print(scissors)
                print("I choose scissors!")

        else:
          print("Invalid Option!")
          continue

        time.sleep(2)

        computer = random.randint(0, 2)
        if computer == 0:
            print(rock)
            print("I choose rock!")
        elif computer == 1:
            print(paper)
            print("I choose paper!")
        else:
            if computer == 2:
                print(scissors)
                print("I choose scissors!")

        if (computer == 0 and user_choice == 1) or (computer == 1 and user_choice == 2) or (computer == 2 and user_choice == 0):
          
            print("\nYou win!")
        elif computer == 1 and user_choice == 0:
            print("\nYou lost!")
        elif computer == 2 and user_choice == 1:
            print("\nYou lost!")
        elif computer == 0 and user_choice == 2:
            print("\nYou lost!")
        elif user_choice == computer:
            print("\nTie!")

        play_again = input("Want to play again? Y/N: ")
        if play_again.lower() == "n":
            print("Bye!")
            break
else:
  if user_input.lower() == "n":
    print("Bye!")
    