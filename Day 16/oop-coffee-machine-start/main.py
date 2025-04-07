from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

test_coffee_maker=CoffeeMaker()
test_money_machine=MoneyMachine()
test_menu=Menu()

is_on=True

while is_on:
    options=test_menu.get_items()
    choice=input(f"What would you like? ({options}) : ").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        test_coffee_maker.report()
        test_money_machine.report()
    else:
        drink=test_menu.find_drink(choice)
        if bool(drink) and test_coffee_maker.is_resource_sufficient(drink) and test_money_machine.make_payment(drink.cost):
            test_coffee_maker.make_coffee(drink)














