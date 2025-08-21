import os
import sys
import time
import shutil
import sqlite3
from Error import error
from datetime import datetime
from Internal import enterDB, addtoDB, exportDB, removefromDB
from Colors import Colors
from INVADERS import really

DATABASE = 'database.db'

def header():
    print(f"{Colors.BRIGHT_GREEN}@@@@@@@@ @@@ @@@      @@@@@@@@@@   @@@@@@      @@@@@@@   @@@@@@  @@@@@@@  @@@@@@  @@@@@@@   @@@@@@   @@@@@@ @@@@@@@@{Colors.RESET}")
    time.sleep(0.25)
    print(f"{Colors.BRIGHT_GREEN}@@!      @@! @@!      @@! @@! @@! !@@          @@!  @@@ @@!  @@@   @@!   @@!  @@@ @@!  @@@ @@!  @@@ !@@     @@!{Colors.RESET}")
    time.sleep(0.25)
    print(f"{Colors.BRIGHT_GREEN}@!!!:!   !!@ @!!      @!! !!@ @!@  !@@!!       @!@  !@! @!@!@!@!   @!!   @!@!@!@! @!@!@!@  @!@!@!@!  !@@!!  @!!!:!{Colors.RESET}")
    time.sleep(0.25)
    print(f"{Colors.BRIGHT_GREEN}!!:      !!: !!:      !!:     !!:     !:!      !!:  !!! !!:  !!!   !!:   !!:  !!! !!:  !!! !!:  !!!     !:! !!:{Colors.RESET}")
    time.sleep(0.25)
    print(f"{Colors.BRIGHT_GREEN} :       :   : ::.: :  :      :   ::.: :       :: :  :   :   : :    :     :   : : :: : ::   :   : : ::.: :  : :: :::{Colors.RESET}")
    breaker(4)

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
    loading_bar(2)
    error()
    breaker(1)
    slowprint(Colors.DIM + "-- BurntCr1sp was here :P --" + Colors.RESET)
    breaker(1)
    really()
    exit()

def loading_bar(duration=2, width=30):
    sys.stdout.write(Colors.CYAN + "[")
    for _ in range(width):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(duration / width)
    sys.stdout.write("]" + Colors.RESET + "\n")

def exportexess():
    try:
        with sqlite3.connect(DATABASE) as conn:
            cur = conn.cursor()
        select_query = """
        SELECT
            *
        FROM Films
        """
        cur.execute(select_query)
        return cur.fetchall()
    except sqlite3.Error as e:
        print(Colors.RED + f">> FDB ERROR: {e}" + Colors.RESET)
        return []

def Main():
    clear()
    slowprint(Colors.RED + Colors.BOLD + ">>> [SECURE TERMINAL ONLINE] <<<" + Colors.RESET)
    slowprint(Colors.DIM + "Initializing FDB access layer..." + Colors.RESET)
    loading_bar(1.5)
    slowprint(Colors.DIM + "Decrypting FDB database..." + Colors.RESET)
    loading_bar(1.2)
    slowprint(Colors.GREEN + Colors.BOLD + Colors.BLINK + "ACCESS GRANTED: FDB STREAM OPEN\n" + Colors.RESET)

    timenow = datetime.now().strftime("%H:%M:%S")
    print(f'{Colors.DIM}[{timenow}]{Colors.RESET} {Colors.BRIGHT_YELLOW}-- COMMANDS --{Colors.RESET}')
    print("1. Enter FDB Database")
    print("2. Search Database")
    print("3. Add to Database")
    print("4. Remove from Database")
    print("5. Export Database")
    print("6. Exit\n")
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

    elif user_input == "search" or user_input == "search database" or user_input == "2":
        ...

    elif user_input == "add" or user_input == "add to database" or user_input == "3":
        clear()
        header()
        loop = True
        while loop == True:
            print("Enter the films name:")
            name = input(f"{Colors.BRIGHT_YELLOW}>>> {Colors.RESET}")
            breaker(1)
            print("Enter the films year of release:")
            year = int(input(f"{Colors.BRIGHT_YELLOW}>>> {Colors.RESET}"))
            breaker(1)
            print("Enter the films rating (e.g PG):")
            rating = input(f"{Colors.BRIGHT_YELLOW}>>> {Colors.RESET}")
            breaker(1)
            print("Enter films length in minutes:")
            length = int(input(f"{Colors.BRIGHT_YELLOW}>>> {Colors.RESET}"))
            breaker(1)
            print("Enter the films genre:")
            genre = input(f"{Colors.BRIGHT_YELLOW}>>> {Colors.RESET}")
            breaker(1)
            result = addtoDB(DATABASE, name, year, rating, length, genre)
            print(result)
            time.sleep(3)
            clear()

            again = input("Go again? (Y/N) ").upper()

            if again == "Y":
                clear()
                pass
            else:
                clear()
                Main()

    elif user_input == "remove" or user_input == "remove from database" or user_input == "4":
        while True:
            clear()
            enterDB()
            print(f"{Colors.BRIGHT_YELLOW}Select a film ID to be deleted: {Colors.RESET}")
            selectedID = int(input(f"{Colors.BRIGHT_YELLOW}>>> {Colors.RESET}"))
            removefromDB(DATABASE, selectedID)

            clear()
            print("Go again? (Y/N)")
            again = input(f"{Colors.BRIGHT_YELLOW}>>> {Colors.RESET}").upper()

            if again != "Y":
                Main()

    elif user_input == "export" or user_input == "export database" or user_input == "5":
        clear()
        print('Are you sure you would like to export? (Y/N)')
        sure = input(f'{Colors.BRIGHT_YELLOW}>>> {Colors.RESET}').lower()
        if sure == "y":
            clear()
            print(f'{Colors.DIM}The file should be named FDB_export.txt... {Colors.RESET}')
            time.sleep(2)
            print(f'{Colors.DIM}Best of luck friend... {Colors.RESET}')
            time.sleep(1.25)
            films = exportexess()
            exportDB(films)
            time.sleep(3)
            clear()
            Main()
        else:
            Main()

    elif user_input == "exit" or user_input == "6":
        clear()
        leave()
Main()