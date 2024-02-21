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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resouces_sufficient(order_ingredients):
    """Returns True when the order can be made ,or False if order cn not be made"""
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print("sorry there is no enough {item}")
            return False
    return True
def process_coins():
    """Return total calculated from coin inserted """
    print("Please insert coin")
    total=int(input("how many quarters?"))*0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many nickles?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    """Return True when payment is accepted, or False if payment is not accepted"""
    if money_received>=drink_cost:
        change=round(money_received-drink_cost, 2)
        print(f"Here is ${change}in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("sorry insufficient money .Money refunded")
        return False
def make_coffee(drink_name,order_ingredients):
    for  item in order_ingredients:
        resources[item]-=order_ingredients[item]
        print(f"here is your {drink_name}☕️")










is_on=True
while is_on:
    choice=input("what you like?(espresso/latte/cappuccino):")
    if choice=="off":
        is_on=False
    elif choice=="report":
       print(f"water:{resources['water']}ml,")
       print(f"milk:{resources['milk']}ml,")
       print(f"coffee:{resources['coffee']}g,")
       print(f"Money:${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_resouces_sufficient(drink["ingredients"]) :
          payment=process_coins()
          if is_transaction_successful(payment,drink['cost']):
              make_coffee(choice,drink["ingredients"])







