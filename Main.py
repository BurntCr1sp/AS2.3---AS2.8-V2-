import os
import sys
import time
import shutil
from Error import error
from datetime import datetime
from Internal import enterDB
from Colors import Colors
from INVADERS import really

def clear():
    os.system('clear')

def print_centered(text):
    width = shutil.get_terminal_size().columns
    padding = max((width - len(text)) // 2, 0)
    print(' ' * padding + text)

def breaker(number):
    for _ in range(number):
        print('')

def slowprint(text, delay=0.015):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    breaker(1)

def leave():
    slowprint(Colors.RED + Colors.BOLD + ">>> [SECURE TERMINAL OFFLINE] <<<" + Colors.RESET)
    slowprint(Colors.DIM + "Encrypting raw data..." + Colors.RESET)
    lol(3)
    error()
    breaker(1)
    slowprint(Colors.DIM + "-- BurntCr1sp was here :P --" + Colors.RESET)
    breaker(1)
    really()
    exit()

def lol(duration=2, width=30):
    sys.stdout.write(Colors.CYAN + "[")
    for _ in range(width):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(duration / width)
    sys.stdout.write("]" + Colors.RESET + "\n")

def Main():
    clear()
    slowprint(Colors.RED + Colors.BOLD + ">>> [SECURE TERMINAL ONLINE] <<<" + Colors.RESET)
    slowprint(Colors.DIM + "Initializing FDB access layer..." + Colors.RESET)
    lol(1.5)
    slowprint(Colors.DIM + "Decrypting FDB database..." + Colors.RESET)
    lol(1.2)
    slowprint(Colors.GREEN + Colors.BOLD + Colors.BLINK + "ACCESS GRANTED: FDB STREAM OPEN\n" + Colors.RESET)

    timenow = datetime.now().strftime("%H:%M:%S")
    print(f'{Colors.DIM}[{timenow}]{Colors.RESET} {Colors.BRIGHT_YELLOW}-- COMMANDS --{Colors.RESET}')
    print("1. Enter FDB Database")
    print("2. Search FDB Database")
    print("3. Add to FDB Database")
    print("4. Export FDB Database")
    print("5. Exit\n")
    user_input = input(Colors.BRIGHT_YELLOW + ">> " + Colors.RESET).lower()

    if user_input == "enter" or user_input == "enter fdb database" or user_input == "1":
        clear()
        enterDB()
        print(f'{Colors.DIM}Back to home or exit? (H/E){Colors.RESET}')
        exit = input(f'{Colors.DIM}>>> {Colors.RESET}').capitalize()

        if exit == 'H':
            Main()
        elif exit == 'E':
            time.sleep(1)
            print(f'{Colors.DIM}Goodbye...{Colors.RESET}')
            time.sleep(2.5)
            clear()
            leave()
        else:
            exit = input('Back to home or exit? (h/e) ').capitalize()

    elif user_input == "search" or user_input == "search fdb database" or user_input == "2":
        ...

    elif user_input == "add" or user_input == "add to fdb database" or user_input == "3":
        ...
    
    elif user_input == "export" or user_input == "export fdb database" or user_input == "4":
        ...

    elif user_input == "exit" or user_input == "5":
        clear()
        leave()
Main()