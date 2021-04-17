water = 400
milk = 540
beans = 120
disposable_cups = 9
money = 550


def remaining():
    print("The coffee machine has:")
    print("{} of water".format(water))
    print("{} of milk".format(milk))
    print("{} of beans".format(beans))
    print("{} of disposable cups".format(disposable_cups))
    print("{} of money".format(money))


def buy():
    kind = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    global disposable_cups
    global milk
    global beans
    global money
    global water
    if kind == '1':
        if water >= 200 and beans >= 16 and disposable_cups >= 1:
            disposable_cups -= 1
            water -= 250
            beans -= 16
            money += 4
        elif water < 200:
            print("Sorry, not enough water!")
    if kind == '2':
        if water >= 200 and beans >= 16 and disposable_cups >= 1 and milk >= 75:
            disposable_cups -= 1
            water -= 350
            milk -= 75
            beans -= 20
            money += 7
        elif milk < 75:
            print("Sorry, not enough milk!")
    if kind == '3':
        if water >= 200 and beans >= 16 and disposable_cups >= 1 and milk >= 75:
            disposable_cups -= 1
            water -= 200
            milk -= 100
            beans -= 12
            money += 6
        elif milk < 75:
            print("Sorry, not enough milk!")
    elif kind == 'back':
        back()
    elif beans < 16:
        print("Sorry, not enough beans!")
    elif disposable_cups < 1:
        print("Sorry, not enough disposable cups!")
    else:
        print("I have enough resources, making you a coffee!")


def fill():
    global disposable_cups
    global milk
    global beans
    global money
    global water
    water += int(input("Write how many ml of water do you want to add:"))
    milk += int(input("Write how many ml of milk do you want to add:"))
    beans += int(input("Write how many grams of coffee beans do you want to add:"))
    disposable_cups += int(input("Write how many disposable cups of coffee do you want to add:"))


def take():
    global money
    print("I gave you ${}".format(money))
    money = 0


def make_action():
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        remaining()
    elif action == 'exit':
        exit(0)


def back():
    make_action()


while make_action != 'exit':
    make_action()
