import os
import sys
import time
import shutil
import sqlite3
from Error import error
from datetime import datetime
from Internal import enterDB
from Colors import Colors

def clear():
    os.system('clear')

def print_centered(text):
    width = shutil.get_terminal_size().columns
    padding = max((width - len(text)) // 2, 0)
    print(' ' * padding + text)

def breaker():
    print('')

def slowprint(text, delay=0.015):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    breaker()

def leave():
    slowprint(Colors.RED + Colors.BOLD + ">>> [SECURE TERMINAL OFFLINE] <<<" + Colors.RESET)
    slowprint(Colors.DIM + "Encrypting raw data..." + Colors.RESET)
    lol(3)
    error()
    breaker()
    slowprint(Colors.DIM + "-- BurntCr1sp was here :P --" + Colors.RESET)
    print(f"""{Colors.RED}
     ▄▄████▄▄
   ▄██████████▄
 ▄██▄██▄██▄██▄██▄
   ▀█▀  ▀▀  ▀█▀
{Colors.RESET}""")
    print(f"""{Colors.BRIGHT_YELLOW}
     ▀▄   ▄▀
    ▄█▀███▀█▄
   █▀███████▀█
   █ █▀▀▀▀▀█ █
      ▀▀ ▀▀
{Colors.RESET}""")
    print(f"""{Colors.ORANGE}
      ▄██▄       
    ▄██████▄
   ███▄██▄███
     ▄▀▄▄▀▄
    ▀ ▀  ▀ ▀
{Colors.RESET}""")
    print(f"""{Colors.GREEN}
   ▄ ▀▄   ▄▀ ▄
   █▄███████▄█
   ███▄███▄███
   ▀█████████▀
    ▄▀     ▀▄
{Colors.RESET}""")
    print(f"""{Colors.BLUE}
    ▄▄████▄▄
   ██████████
   ██▄▄██▄▄██
    ▄▀▄▀▀▄▀▄
   ▀        ▀
{Colors.RESET}""")
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
    print("2. Exit\n")
    user_input = input(Colors.BRIGHT_YELLOW + ">> " + Colors.RESET).lower()

    if user_input == "enter" or user_input == "enter fdb database" or user_input == "1":
        clear()
        enterDB()

    elif user_input == "exit" or user_input == "2":
        clear()
        leave()
Main()


#print(f"""{Colors.BRIGHT_GREEN}@@@@@@@@ @@@ @@@      @@@@@@@@@@   @@@@@@      @@@@@@@   @@@@@@  @@@@@@@  @@@@@@  @@@@@@@   @@@@@@   @@@@@@ @@@@@@@@
#@@!      @@! @@!      @@! @@! @@! !@@          @@!  @@@ @@!  @@@   @@!   @@!  @@@ @@!  @@@ @@!  @@@ !@@     @@!     
#@!!!:!   !!@ @!!      @!! !!@ @!@  !@@!!       @!@  !@! @!@!@!@!   @!!   @!@!@!@! @!@!@!@  @!@!@!@!  !@@!!  @!!!:!  
#!!:      !!: !!:      !!:     !!:     !:!      !!:  !!! !!:  !!!   !!:   !!:  !!! !!:  !!! !!:  !!!     !:! !!:     
# :       :   : ::.: :  :      :   ::.: :       :: :  :   :   : :    :     :   : : :: : ::   :   : : ::.: :  : :: :::{Colors.RESET}""")

"""
░░░░░▀▄░░░▄▀░░░░░
░░░░▄█▀███▀█▄░░░░
░░░█▀███████▀█░░░
░░░█░█▀▀▀▀▀█░█░░░
░░░░░░▀▀░▀▀░░░░░░
░░░░░░░░░░░░░░░░░░
░░░░░▄▄████▄▄░░░░░
░░░▄██████████▄░░░
░▄██▄██▄██▄██▄██▄░
░░░▀█▀░░▀▀░░▀█▀░░░
░░░░░░░░░░░░░░░░░░
░░░▄░▀▄░░░▄▀░▄░░░
░░░█▄███████▄█░░░
░░░███▄███▄███░░░
░░░▀█████████▀░░░
░░░░▄▀░░░░░▀▄░░░░
░░░░░░░░░░░░░░░░░
░░░░▄▄████▄▄░░░░░
░░░██████████░░░░
░░░██▄▄██▄▄██░░░░
░░░░▄▀▄▀▀▄▀▄░░░░░
░░░▀░░░░░░░░▀░░░░"""