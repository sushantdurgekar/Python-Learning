
import random
import art



print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_no=random.randint(1,100)

def choose_a_difficulty():
    difficulty = input(
        "Choose a difficulty. Type 'easy' or 'hard':").lower()
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5
    else:
        print("Invalid Input You get 0 chances")
        return 0

no_of_chance=choose_a_difficulty()

def check_for_answer(g_num, r_no, turns):
    if g_num==r_no:
        print(f"You got it! The answer was {g_num}")
        return -1
    elif g_num>r_no:
        print("Too High")
        return turns-1
    elif g_num<r_no:
        print("Too Low")
        return turns-1


print(f"You have {no_of_chance} attempts remaining to guess the "
      f"number.")

for i in range(0,no_of_chance):
    guess_num=int(input("Make a guess:"))
    no_of_chance=check_for_answer(guess_num,random_no,no_of_chance)
    if no_of_chance==-1:
        break
    elif no_of_chance!=0:
        print("Guess again.")
        print(f"You have {no_of_chance} attempts remaining to guess the "
              "number.")
    else:
        print("You've run out of guesses. Refresh the page to run again.")
        break















