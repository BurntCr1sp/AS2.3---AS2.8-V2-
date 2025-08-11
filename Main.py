import os
import sys
import time
import shutil
import sqlite3
from Error import error
from datetime import datetime
from Internal_Functions import enterDB

class Colors: #Found Parts of List on Stack Overflow
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    ORANGE = '\033[38;5;208m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GRAY = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    INVERT = '\033[7m'

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
    print(f"""{Colors.ORANGE}
      ▄██▄       
    ▄██████▄
   ███▄██▄███
     ▄▀▄▄▀▄
    ▀ ▀  ▀ ▀
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