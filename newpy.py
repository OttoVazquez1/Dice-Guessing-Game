import random
import keyboard
GUESSED = False
def DiceGame():
    print("\n\nLanguage:\n 1.English\n 2.Español")
    while True:
        if keyboard.is_pressed("1"):
            English()
            break
        elif keyboard.is_pressed("2"):
            Español()
            break

def English():
    try:
        print("\033[1;32;40m Welcome to Dice Guesser! \nThe game where you have to guess in which side the dice landed!")
        number = GetNumb()
        TryEng(number)
    except KeyboardInterrupt:
        print("\n\nYou exited the game! Come back soon!")

def Español():
    try:
        print("\n\n\nBienvenido a Dice Guesser! \nEl juego en el que tienes que adivinar en que cara cae el dado!")
        numero = GetNumb()
        TryEsp(numero)
    except KeyboardInterrupt:
        print("\n\nUsted ha abandonado el juego! Vuelva pronto")

def GetNumb():
    number = random.randint(1, 6)
    return number

def TryEng(number):
    tries = 2
    print("Guess a number between 1 - 6!")
    while True:
        try:
            guess = int(input("My answer is:  "))
            if guess not in (1, 2, 3, 4, 5, 6):
                print("Oh oh! I told you to choose a number between 1 and 6! Try again")
            else:
                guessed = ValidateAnswer(number, guess)
                if guessed == False and tries > 0:
                    tries -= 1
                    print("Too bad, that wasn't it. Try again!")
                    pass
                elif guessed == True:
                    print("Amazing, you won!")
                    TryAgainEng()
                    break
                elif tries <= 0:
                    print("You've run out of tries!")
                    TryAgainEng()
                    break
        except ValueError:
            print("Error! Try using numbers for your guess!\n")

def TryEsp(numero):
    
    intentos = 2    
    print("Adivine un numero del 1 al 6! Tienes 3 oportunidades.")
    while True:
        try:
            guess = int(input("Mi respuesta es: "))
            if guess not in (1, 2, 3, 4, 5, 6):
                print("Oh oh! Te dije que elijas un numero del 1 al 6! Vuelve a intentarlo.")
            else:
                guessed = ValidateAnswer(numero, guess)
                if guessed == False and intentos > 0:
                    intentos -= 1
                    print("Ese no era! Prueba otra vez\n")
                    pass
                elif guessed == True:
                    print("Lo has logrado! Increible!\n")
                    TryAgainEsp()
                    break
                elif intentos <= 0:
                    print("Oh no, te has quedado sin intentos!")
                    TryAgainEsp()
                    break
        except ValueError:
            print("Ha ocurrido un error! Verifica que haya usado un número!")

def ValidateAnswer(numero, guess):
    if guess == numero:
        return True
    else:
        return False

def TryAgainEsp():
    print("\nQuieres probar tu suerte otra vez? Presiona Y para si, N para no.")
    while True:
        if keyboard.is_pressed("y"):
            Español()
            break
        if keyboard.is_pressed("n"):
            print("\n\nVuelva pronto!")
            break

def TryAgainEng():
    print("Would you like to try your luck again? Press Y if yes, N if no.")
    while True:
        if keyboard.is_pressed("y"):
            English()
            break
        elif keyboard.is_pressed("n"):
            print("\n\nCome back soon!")
            break
DiceGame()