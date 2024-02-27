

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
    "water": 500,
    "milk": 350,
    "coffee": 200,
}

profit = 0
total_entered_money = 0


def write_report():
    for item in resources:
        print(f"{item}: {resources[item]}")

    print(f"${profit}")


def process_coins():
    print("Please insert coins.")
    Quarter = float(input("how many quarters?:"))
    Dimes = float(input("how many dimes?:"))
    Nickles = float(input("how many nickles?:"))
    Pennies = float(input("how many pennies?:"))
    entered_money = Pennies * 0.01 + Dimes * 0.10 + Nickles * 0.05 + Quarter * 0.25
    return entered_money


def is_transaction_successful(type_of_coffee, payment1):
    coffee_cost = MENU[type_of_coffee]["cost"]

    returned_money = payment1 - coffee_cost
    global total_entered_money
    total_entered_money = + returned_money

    if returned_money >= 0:
        global profit
        profit += coffee_cost
        print(f"Here is ${returned_money} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def is_resources_sufficient(type_of_coffee):
    ingredient = ""
    for key in MENU[type_of_coffee]["ingredients"]:
        if MENU[type_of_coffee]["ingredients"][key] > resources[key]:
            ingredient += key
            print(f"Sorry there is not enough {ingredient}")
            return False

        else:
            resources[key] -= MENU[type_of_coffee]["ingredients"][key]
        return True


def fill_machine():
    add_item = input("Which item do you want to add? 'w' water or 'm' milk or 'c' coffee: ")
    amount_of_item = int(input("How much ?: "))

    if add_item == "w":
        resources["water"] += amount_of_item
    elif add_item == "m":
        resources["milk"] += amount_of_item

    elif add_item == "c":
        resources["coffee"] += amount_of_item

    else:
        print("invalid input")

    continue_to_adding = input("Do you want to continuo to adding process? 'y' yes or 'n' no: ")

    if continue_to_adding == "y":
        fill_machine()


def make_coffee():
    is_continue = True
    while is_continue:
        selected_process = input("What would you like? (espresso/latte/cappuccino):")
        if selected_process == "report":
            write_report()

        elif selected_process == "off":
            is_continue = False

        elif selected_process == "latte" or selected_process == "espresso" or selected_process == "cappuccino":
            payment = process_coins()
            if is_resources_sufficient(selected_process) == True and is_transaction_successful(selected_process, payment) == True:
                is_continue = True
                print(f"Here is your {selected_process} ☕️. Enjoy!")

            else:
                is_continue = False

        elif selected_process == "fill_machine":
            fill_machine()

        else:
            print("Invalid input. Please try again !!")
            make_coffee()

        answer = input("Do you want new process('y' yes or 'n' no):")
        if answer == "y":
            make_coffee()

        elif answer == "n":
            is_continue = False


make_coffee()
