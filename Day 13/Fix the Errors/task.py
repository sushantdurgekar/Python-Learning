
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You've typed and invalid number. Please try again with "
          "numerical response such as 14.")
    age = int(input("How old are you?"))


if age > 18:
    print(f"You can drive at age {age}.")
