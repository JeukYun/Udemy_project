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


def coin():
    print("Please insert coin")
    quarter = float(input("how many quarters?"))
    dime = float(input("how many dimes?"))
    nickle = float(input("how many nickles?"))
    pennie = float(input("how many pennies?"))
    return quarter, dime, nickle, pennie


def check_change(Q, D, N, P, order):
    total = (Q * 0.25) + (D * 0.1) + (N * 0.05) + (P * 0.01)
    change = total - float(MENU[order]["cost"])
    if total < MENU[order]["cost"]:
        print("Sorry that's not enough money.")
        print(f'{order} is ${MENU[order]["cost"]}, money refunded.')
    elif total == MENU[order]["cost"]:
        print(f'Here is your {order}. Enjoy!')
    else :
        print(f'Here is ${change} in change!')


def check_ingredient(order):
    ingredient = MENU[order]["ingredients"]
    if order == "espresso":

        if int(ingredient["water"]) > int(resources["water"]):
            print('Sorry there is not enough water.')
        elif int(ingredient["coffee"]) > int(resources["coffee"]):
            print('Sorry there is not enough coffee.')
        else:
            quarter, dime, nickle, pennie = coin()
            check_change(quarter, dime, nickle, pennie, order)

        return {"water" : int(resources["water"]) - int(ingredient["water"]),
            "milk" : int(resources["milk"]),
            "coffee": int(resources["coffee"]) - int(ingredient["coffee"])}

    elif order == "latte" or "cappuccino":

        if int(ingredient["water"]) > int(resources["water"]):
            print('Sorry there is not enough water.')
        elif int(ingredient["milk"]) > int(resources["milk"]):
            print('Sorry there is not enough milk.')
        elif int(ingredient["coffee"]) > int(resources["coffee"]):
            print('Sorry there is not enough coffee.')
        else:
            quarter, dime, nickle, pennie = coin()
            check_change(quarter, dime, nickle, pennie, order)

    return {"water" : int(resources["water"]) - int(ingredient["water"]),
            "milk" : int(resources["milk"]) - int(ingredient["milk"]),
            "coffee": int(resources["coffee"]) - int(ingredient["coffee"])}


def coffe_machine(order):
    if order == "report":
        print(f'water : {resources["water"]}\nmilk : {resources["milk"]}'
              f'\ncoffee : {resources["coffee"]}')
        return resources
    elif order == "espresso" or "latte" or "cappuccino":
        ingredient = check_ingredient(order)
    return ingredient


enough = True

while enough:
    print(f'espresso is ${MENU["espresso"]["cost"]}, '
          f'latte is ${MENU["latte"]["cost"]}, '
          f'cappuccino is ${MENU["cappuccino"]["cost"]}')
    coffe = input("What would you like? (espresso/latte/cappuccino)")

    resources = coffe_machine(coffe)
    for i in resources:
        if resources[i] < 0 :
            enough = False
