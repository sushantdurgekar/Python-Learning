import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator_dictionary={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    accumulate=True
    num1=float(input("What's the first number?: "))
    while accumulate:
        operation=input("+\n-\n*\n/\nPick and operation: ")
        num2=float(input("What's the next number?: "))

        output = calculator_dictionary[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {output}")
        need_to_continue=input(f"Type 'y' to continue calculating with "
                               f"{output}, or type 'n' to start new "
                               f"calculation: ").lower()
        if need_to_continue=='y':
            accumulate=True
            num1=output
        elif need_to_continue=='n':
            accumulate=False
            calculator()
        else:
            print("Invalid Input")
            break

calculator()

