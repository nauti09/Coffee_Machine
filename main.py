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


def get_report():
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}gm\nMoney: ${money}\n"


def check_resources(coffee_type):
    if resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    elif resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return False
    return True


def process_coins(quarter,dimes,nickel,penny):
    total_vaule = quarter * 0.25 + dimes * 0.1 + nickel * 0.05 + penny * 0.01
    return total_vaule


def transaction_status(money_inserted, coffee_type):
    if money_inserted < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif money_inserted > MENU[coffee_type]["cost"]:
        change = money_inserted - MENU[coffee_type]["cost"]
        change = round(change,2)
        print(f"Here is ${change:.2f} dollars in change.")
        return money_inserted - change
    return money_inserted


def make_coffee(coffee_choice):
    resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
    resources["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]
    print(f"Here is your {coffee_choice}. Enjoy!")


off = False
money = 0

while not off:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if coffee_choice == "off":
        off = True
    elif coffee_choice == "report":
        report = get_report()
        print(report)
    elif check_resources(coffee_choice):
        quarter = int(input("How many quarters?:"))
        dimes = int(input("How many dimes?:"))
        nickel = int(input("How many nickel?:"))
        penny = int(input("How many pennies?:"))
        money_inserted = process_coins(quarter, dimes, nickel, penny)
        money_earned = transaction_status(money_inserted,coffee_choice)
        money += money_earned
        if money_earned != 0:
            make_coffee(coffee_choice)

