from coffee_machine_data import MENU,resources

COFFEE_RESOURCES=resources
MONEY=0
QUARTERS=0.25
DIMES=0.1
NICKLES=0.05
PENNIES=0.01

# TODO 1: Prompt user by asking “What would you like? (
#  espresso/latte/cappuccino):”
# # a. Check the user’s input to decide what to do next.
# # b. The prompt should show every time action has completed,
# e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

# TODO 5 and 6: Process coins... and Check transaction successful?
def processing_coins(coffee_type):
    global MONEY
    required_coins=MENU[coffee_type]["cost"]
    print("Please insert coins.")
    total=float(input("how many quarters?: "))*QUARTERS
    total+=float(input("how many dimes?: "))*DIMES
    total+=float(input("how many nickles?: "))*NICKLES
    total+=float(input("how many pennies?: "))*PENNIES
    if total>=required_coins:
        MONEY+=required_coins
        coin_change=round(total-required_coins,2)
        if coin_change==0:
            print("Money Accepted")
        else:
            print(f"Money Accepted, Here is ${coin_change} in "
                    f"change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# TODO 4: Check resources sufficient?
def is_resource_sufficient(coffee_type):
    drink_items=MENU[coffee_type]["ingredients"]
    for item in drink_items:
        if COFFEE_RESOURCES[item]<drink_items[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

#  TODO 7: Make Coffee. and deduct resources
def deduct_coffee_items(coffee_type):
    global COFFEE_RESOURCES
    drink_items = MENU[coffee_type]["ingredients"]
    COFFEE_RESOURCES["water"]-=drink_items["water"]
    COFFEE_RESOURCES["coffee"]-=drink_items["coffee"]
    if "milk" in drink_items:
        COFFEE_RESOURCES["milk"]-=drink_items["milk"]


def make_coffee(coffee_type):
    check_resources=is_resource_sufficient(coffee_type)
    if check_resources:
        check_coins=processing_coins(coffee_type)
        if check_coins:
            deduct_coffee_items(coffee_type)
            print(f"Here is your {coffee_type} ☕️. Enjoy!")


# TODO 3: Print report.
def give_report():
    """Prints the available resources"""
    print(f"Water: {COFFEE_RESOURCES["water"]}ml\nMilk: "
          f"{COFFEE_RESOURCES["milk"]}ml\nCoffee: "
          f"{COFFEE_RESOURCES["coffee"]}g\nMoney: ${MONEY}")


coffee_machine_is_on=True
while coffee_machine_is_on:
    coffee_machine_inputs=input("What would you like? (espresso/latte/cappuccino):").lower()
    if coffee_machine_inputs=='off':
        coffee_machine_is_on=False
    elif coffee_machine_inputs=="report":
        give_report()
    elif (coffee_machine_inputs=="espresso" or
          coffee_machine_inputs=="latte" or
          coffee_machine_inputs=="cappuccino"):
        make_coffee(coffee_machine_inputs)
    else:
        print("Invalid Input!!!! Please try again")

