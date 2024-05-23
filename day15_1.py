MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
logo = """
||==============================================================================================||                     
||                        _____ ____  ______ ______ ______ ______                               ||  
||                       / ____/ __ \|  ____|  ____|  ____|  ____|                              ||    
||                      | |   | |  | | |__  | |__  | |__  | |__                                 ||         
||                      | |   | |  | |  __| |  __| |  __| |  __|                                ||  
||                      | |___| |__| | |    | |    | |____| |____                               ||      
||                       \_____\____/|_|    |_|    |______|______|                              ||        
||                                                                                              ||     
||==============================================================================================||                                                                
"""

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

Money = 0


def Make_coffee(odered,paid):
    cost = (MENU[odered])["cost"]
    change = paid-cost
    global Money 
    Money += cost
    current_inged = (MENU[odered])["ingredients"]


    resources["coffee"] -= current_inged["coffee"]
    resources["milk"] -=current_inged["milk"]
    resources["water"] -= current_inged["water"]

    print(f"Here is your change {change}")
    print(f"Here is your {odered}! enjoy it.")


def payment():
    Quater = (float(input("how many Quater? :")))*0.25
    pennies = float(input("how many Pennies? :"))*0.01
    dimes = float(input("how many Dimes? :"))*0.10
    nickles = float(input("how many nickles? :"))*0.05
    total = round((Quater+pennies+dimes+nickles),2)
    print(f"Your total payment is {total}")
    return total


def check_resource(Ask):
    Current_ask = MENU[Ask]
    ingredient = Current_ask["ingredients"]
    ask_water = ingredient["water"]
    ask_milk = ingredient["milk"]
    ask_coffee = ingredient["coffee"]
    if resources["coffee"] >= ask_coffee and resources["milk"] >= ask_milk and resources["water"] >= ask_water:
        return True
    else:
        print("Oh! sorry insuffecient resource.")


def coffee(oredr):

    if check_resource(oredr):
        paid = payment()
        if paid >= (MENU[oredr])["cost"]:
            Make_coffee(oredr,paid)
        else:
            print(f"Insuffecient payment, take it back{paid}")
            

def take_order():
    should_continue = False
    print(logo)
    while not should_continue:
        user_req = input("What would you like? (espresso/latte/cappuccino):").lower()
        if not (user_req == "off" or user_req == "report"):
            coffee(user_req)
        elif user_req == "off":
            should_continue = True
            print("Thanks visit again")

        elif user_req == "report":
            print(resources)


take_order()
