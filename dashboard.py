
import os
import sys
import socket
import platform
import datetime
import time
import random

# Terminal colors
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def clear():
    os.system("cls")


def header():
    print(GREEN + "=" * 48)
    print("             CYBER TERMINAL")
    print("                VERSION 1.0")
    print("=" * 48 + RESET)


def system_info():
    clear()
    header()

    print(CYAN + "\n[ SYSTEM INFORMATION ]")
    print("Computer:", socket.gethostname())
    print("OS:", platform.system())
    print("OS Version:", platform.version())
    print("Python:", sys.version.split()[0])

    input("\nPress ENTER to return...")


def network_info():
    clear()
    header()

    print(CYAN + "\n[ NETWORK INFORMATION ]")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print("Local IP:", s.getsockname()[0])
        s.close()
    except OSError:
        print("Local IP: Unavailable")

    print("Hostname:", socket.gethostname())

    input("\nPress ENTER to return...")


def live_clock():
    while True:
        clear()
        header()

        print(YELLOW + "\n[ LIVE CLOCK ]")
        print(datetime.datetime.now().strftime("%H:%M:%S"))
        print("\nPress CTRL+C to return.")

        time.sleep(1)


def animation():
    chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    try:
        while True:
            line = ""

            for i in range(65):
                line += random.choice(chars)

            print(GREEN + line + RESET)
            time.sleep(0.1)

    except KeyboardInterrupt:
        pass


def games():
    clear()
    header()

    number = random.randint(1, 10)

    print(CYAN + "\n[ NUMBER GUESSING GAME ]")

    while True:
        try:
            guess = int(input("Guess a number (1-10): "))

            if guess == number:
                print(GREEN + "YOU WIN!" + RESET)
                break
            elif guess > number:
                print(YELLOW + "Too high!" + RESET)
            else:
                print(YELLOW + "Too low!" + RESET)

        except ValueError:
            print(RED + "Enter a valid number!" + RESET)

    input("\nPress ENTER to return...")


def main_menu():

    while True:
        clear()
        header()

        print(CYAN + """
       [ SYSTEM CONTROL CENTER ]

       1. SYSTEM INFORMATION
       2. NETWORK INFORMATION
       3. LIVE CLOCK
       4. ASCII ANIMATION
       5. CYBER GAMES
       6. EXIT
        """ + RESET)

        choice = input("SELECT AN OPTION: ")

        if choice == "1":
            system_info()

        elif choice == "2":
            network_info()

        elif choice == "3":
            try:
                live_clock()
            except KeyboardInterrupt:
                pass

        elif choice == "4":
            animation()

        elif choice == "5":
            games()

        elif choice == "6":
            clear()
            print(GREEN + "TERMINAL CLOSED. GOODBYE!" + RESET)
            break

        else:
            print(RED + "INVALID OPTION!" + RESET)
            time.sleep(1)


main_menu()
