import sqlite3
from Colors import Colors
import time
import sys
import os

DATABASE = 'database.db'

def useless(number):
    for _ in range(number):
        print('')

def lol2(duration=2, width=114):
    sys.stdout.write(Colors.CYAN + "[")
    for _ in range(width):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(duration / width)
    sys.stdout.write("]" + Colors.RESET + "\n")

def enterDB():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        select_query = """
        SELECT
            *
        FROM Films
        """

        print(f"{Colors.RED}@@@@@@@@ @@@ @@@      @@@@@@@@@@   @@@@@@      @@@@@@@   @@@@@@  @@@@@@@  @@@@@@  @@@@@@@   @@@@@@   @@@@@@ @@@@@@@@{Colors.RESET}")
        time.sleep(0.25)
        print(f"{Colors.RED}@@!      @@! @@!      @@! @@! @@! !@@          @@!  @@@ @@!  @@@   @@!   @@!  @@@ @@!  @@@ @@!  @@@ !@@     @@!{Colors.RESET}")
        time.sleep(0.25)
        print(f"{Colors.RED}@!!!:!   !!@ @!!      @!! !!@ @!@  !@@!!       @!@  !@! @!@!@!@!   @!!   @!@!@!@! @!@!@!@  @!@!@!@!  !@@!!  @!!!:!{Colors.RESET}")
        time.sleep(0.25)
        print(f"{Colors.RED}!!:      !!: !!:      !!:     !!:     !:!      !!:  !!! !!:  !!!   !!:   !!:  !!! !!:  !!! !!:  !!!     !:! !!:{Colors.RESET}")
        time.sleep(0.25)
        print(f"{Colors.RED} :       :   : ::.: :  :      :   ::.: :       :: :  :   :   : :    :     :   : : :: : ::   :   : : ::.: :  : :: :::{Colors.RESET}")
        useless(4)
        print(f"{Colors.DIM}Importing FDB...{Colors.RESET}")
        lol2(3)
        useless(1)
        print(f"{Colors.DIM}Just a random loading bar for suspence and to waste time...{Colors.RESET}")
        lol2(3)
        print(f"{Colors.DIM}W̷e̴l̵c̷o̷m̴e̶...{Colors.RESET}")
        time.sleep(2)
        os.system('clear')
        print(f"{Colors.BRIGHT_GREEN}@@@@@@@@ @@@ @@@      @@@@@@@@@@   @@@@@@      @@@@@@@   @@@@@@  @@@@@@@  @@@@@@  @@@@@@@   @@@@@@   @@@@@@ @@@@@@@@{Colors.RESET}")
        time.sleep(0.25)
        print(f"{Colors.BRIGHT_GREEN}@@!      @@! @@!      @@! @@! @@! !@@          @@!  @@@ @@!  @@@   @@!   @@!  @@@ @@!  @@@ @@!  @@@ !@@     @@!{Colors.RESET}")
        time.sleep(0.25)
        print(f"{Colors.BRIGHT_GREEN}@!!!:!   !!@ @!!      @!! !!@ @!@  !@@!!       @!@  !@! @!@!@!@!   @!!   @!@!@!@! @!@!@!@  @!@!@!@!  !@@!!  @!!!:!{Colors.RESET}")
        time.sleep(0.25)
        print(f"{Colors.BRIGHT_GREEN}!!:      !!: !!:      !!:     !!:     !:!      !!:  !!! !!:  !!!   !!:   !!:  !!! !!:  !!! !!:  !!!     !:! !!:{Colors.RESET}")
        time.sleep(0.25)
        print(f"{Colors.BRIGHT_GREEN} :       :   : ::.: :  :      :   ::.: :       :: :  :   :   : :    :     :   : : :: : ::   :   : : ::.: :  : :: :::{Colors.RESET}")
        
        cursor.execute(select_query)
        data1 = cursor.fetchall()
        print('')
        print('                         〰〰 DATA 〰〰')
        print('╭────┬────────────────┬──────────┬─────────┬───────────┬─────────╮')
        print('│ ID │ Name           │ Year     │  Rating │  Length   │  Genre  │')
        print('├────┼────────────────┼──────────┼─────────┼───────────┼─────────┤')
        for data in data1:
            print(f"│{data[0]:<4}│{data[1]:<16}│{data[2]:<10}│{data[3]:<9}│{data[4]:<11}│{data[5]:<9}│")
        print('╰────┴────────────────┴──────────┴─────────┴───────────┴─────────╯')
        











#print(f"""{Colors.BRIGHT_GREEN}@@@@@@@@ @@@ @@@      @@@@@@@@@@   @@@@@@      @@@@@@@   @@@@@@  @@@@@@@  @@@@@@  @@@@@@@   @@@@@@   @@@@@@ @@@@@@@@
#@@!      @@! @@!      @@! @@! @@! !@@          @@!  @@@ @@!  @@@   @@!   @@!  @@@ @@!  @@@ @@!  @@@ !@@     @@!     
#@!!!:!   !!@ @!!      @!! !!@ @!@  !@@!!       @!@  !@! @!@!@!@!   @!!   @!@!@!@! @!@!@!@  @!@!@!@!  !@@!!  @!!!:!  
#!!:      !!: !!:      !!:     !!:     !:!      !!:  !!! !!:  !!!   !!:   !!:  !!! !!:  !!! !!:  !!!     !:! !!:     
# :       :   : ::.: :  :      :   ::.: :       :: :  :   :   : :    :     :   : : :: : ::   :   : : ::.: :  : :: :::{Colors.RESET}""")
