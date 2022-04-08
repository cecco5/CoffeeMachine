"""Macchina del caffè che distribuisce tre tipi di bevande:
- espresso
- latte
- cappuccino"""


# Risorse presenti nella macchina
risorse = {"milk": 300,
           "coffee": 300,
           "water": 300
           }

# Credito
profit = 0

# Menu macchina
MENU = {
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

    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 24,
        },
        "cost": 2.5,
    }
}

# Messaggio display iniziale


def benvenuto():
    comando = input("Salve. Cosa desidera? (espresso/latte/cappuccino): ")
    return comando

# Verifica disponibilità risorse per la bevanda richiesta


def check_resources(ingredienti):
    """Ritorna True se le risorse sono sufficienti per la richiesta, false altrimenti"""
    for item in ingredienti:
        if ingredienti[item] >= risorse[item]:
            print("Spiacenti, non c'è abbastanza {}".format(item))
            return False
    return True

# Aggiorna le risorse dopo la vendita di una bevanda


def update_resources(ingredienti):
    """Aggiorna le risorse della macchina sottraendo gli ingredienti dell'ordine"""
    for item in ingredienti:
        risorse[item] -= ingredienti[item]


# Genera report sulle risorse della macchina
def report_2():
    """Stampa l'elenco delle risorse disponibili nella macchina"""
    print(f"Milk: {risorse['milk']}ml")
    print(f"Water: {risorse['water']}ml")
    print(f"Coffee: {risorse['coffee']}ml")
    print(f"Money: {profit}$")


def report():
    """Stampa l'elenco delle risorse disponibili nella macchina"""
    for ingrediente in risorse:
        print("{}: {}".format(ingrediente, risorse[ingrediente]))
    print(f"money: {profit}$")


def process_coins():
    """"Ritorna il totale calcolato dalle monete inserite"""
    print("Prego, inserire le monete.")
    total = int(input("Quanti quarters?: ")) * 0.25
    total += int(input("Quanti dimes?: ")) * 0.1
    total += int(input("Quanti nickels?: ")) * 0.05
    total += int(input("Quanti pennies?: ")) * 0.01
    return total


def check_transaction(pagamento, costo_bevanda):
    """Ritorna True se il pagamento è sufficiente per l'acquisto. Ritorna False se non è sufficiente"""
    if pagamento < costo_bevanda:
        print("Mi dispiace, non hai inserito abbastanza monete. Restituzione monete in corso...")
        return False
    resto = round(pagamento - costo_bevanda, 2)
    print(f"Resto: {resto}$")
    global profit
    profit += costo_bevanda
    return True


# INIZIO PROGRAMMA

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
