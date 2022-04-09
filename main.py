from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    comando = input("Salve. Cosa desidera? (espresso/latte/cappuccino): ")
    if comando == "report":
        coffee_maker.report()
        money_machine.report()
    elif comando == "off":
        is_on = False
    elif comando == "espresso" or comando == "latte" or comando == "cappuccino":
        menu = Menu()
        drink = menu.find_drink(comando)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print("Comando non disponibile\n")









'''
# Flusso continuo programma
is_on = True

while is_on:
    comando_utente = benvenuto()
    if comando_utente == "report":
        report_2()
    elif comando_utente == "off":
        is_on = False
    elif comando_utente == "espresso" or comando_utente == "latte" or comando_utente == "cappuccino":
        bevanda = MENU[comando_utente]
        if check_resources(bevanda["ingredients"]):
            pagamento = process_coins()
            if check_transaction(pagamento, bevanda["cost"]):
                update_resources(bevanda["ingredients"])
                print(f"Ecco il suo {comando_utente}.")
    else:
        print("Comando non disponibile\n")
'''
