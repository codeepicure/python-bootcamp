from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


current_selection = "on"
my_menu = Menu()
my_coffeeMaker = CoffeeMaker()
my_moneyMachine = MoneyMachine()

while current_selection != "off":
    current_selection = input(f"What would you like? {my_menu.get_items()}: ")

    if current_selection == "report":
        my_coffeeMaker.report()
        my_moneyMachine.report()
        continue

    selected_drink = my_menu.find_drink(current_selection)

    if selected_drink is None:
        continue

    if not my_coffeeMaker.is_resource_sufficient(selected_drink):
        continue

    enough_money = my_moneyMachine.make_payment(selected_drink.cost)

    if not enough_money:
        continue

    my_coffeeMaker.make_coffee(selected_drink)


