MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_revenue = 0.0
current_order = "on"
user_payment = 0.0


def print_report():
    print(f"""
        Water: {resources["water"]}
        Milk: {resources["milk"]}
        Coffee: {resources["coffee"]}
        Money: ${total_revenue}
    """)


def check_order_type(user_order):
    for drink in MENU:
        if user_order == drink:
            return True

    return False


def check_sufficient_resources(user_order):
    requested_drink_ingredients = MENU[user_order]["ingredients"]

    for ingredient in requested_drink_ingredients:
        if requested_drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False

    return True


def collect_coins():
    global user_payment
    user_payment = float(input("How many quarters? ")) * 0.25
    user_payment += float(input("How many dimes? ")) * 0.10
    user_payment += float(input("How many nickles? ")) * 0.05
    user_payment += float(input("How many cents? ")) * 0.01


def check_if_coins_sufficient(user_order):
    if user_payment >= MENU[user_order]["cost"]:
        return True

    print(f"Insufficient funds, refunded ${user_payment}")


def create_drink(user_order):
    global total_revenue
    global user_payment
    total_revenue += MENU[user_order]["cost"]
    requested_drink_ingredients = MENU[user_order]["ingredients"]

    for ingredient in requested_drink_ingredients:
        resources[ingredient] -= requested_drink_ingredients[ingredient]

    print(f"Enjoy your {user_order}!")

    if user_payment > MENU[user_order]["cost"]:
        print(f"Here's your change: ${user_payment - MENU[user_order]['cost']}")


while current_order != "off":
    current_order = input("What would you like? (espresso/latte/cappuccino): ")
    if current_order == "off":
        break

    if current_order == "report":
        print_report()
        continue

    if not check_order_type(current_order):
        print("I'm sorry we do not have this kind of drink.")
        continue

    if not check_sufficient_resources(current_order):
        continue

    collect_coins()

    if not check_if_coins_sufficient(current_order):
        continue

    create_drink(current_order)

