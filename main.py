from resource import MENU, resources
profit = 0

def is_resource_sufficient(order_ingredients):
    """Vrátí True pokud je dost surovin, False pokud není"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"V přístroji není dostatek {item}!")
            return False
    return True

def process_coins():
    """Vrátí součet vložených peněz"""
    total = int(input("Vložte peníze:  "))
    return total


def is_transaction_successful(money_received, cost_of_drink):
    """"Vrátí True pokud je vloženo dostatek peněz a False pokud není"""
    if money_received >= cost_of_drink:
        change = money_received - cost_of_drink
        print(f"Vracíme {change} Kč.")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Nevložil jste dost peněz, peníze vracíme!")
        return False

def make_coffee(drink_name, order_ingredients):
    """Odečte ingredience objednávky ze zásob ingrediencí v přístroji"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Objednávka: {drink_name} je hotova!")
    print("Prosím, vezměte si svou objednávku!")

is_on = True

while is_on:
    choice = input("Co si dáte? (espresso, latte, cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print("V kávovaru je:")
        print(f"Voda: {resources['water']}ml")
        print(f"Mléko: {resources['milk']}ml")
        print(f"Káva: {resources['coffee']}g")
        print(f"{profit} Kč")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



