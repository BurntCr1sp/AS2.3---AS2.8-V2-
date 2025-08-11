import sqlite3
from Colors import Colors
import time
import sys
import os

DATABASE = 'DataBase.db'

def useless():
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
        FROM 'Films'
        """
        cursor.execute(select_query)
        data = cursor.fetchall()
        print(f"{Colors.RED}@@@@@@@@ @@@ @@@      @@@@@@@@@@   @@@@@@      @@@@@@@   @@@@@@  @@@@@@@  @@@@@@  @@@@@@@   @@@@@@   @@@@@@ @@@@@@@@{Colors.RESET}")
        time.sleep(0.25)
        print(f"{Colors.RED}@@!      @@! @@!      @@! @@! @@! !@@          @@!  @@@ @@!  @@@   @@!   @@!  @@@ @@!  @@@ @@!  @@@ !@@     @@!{Colors.RESET}")
        time.sleep(0.25)
        print(f"{Colors.RED}@!!!:!   !!@ @!!      @!! !!@ @!@  !@@!!       @!@  !@! @!@!@!@!   @!!   @!@!@!@! @!@!@!@  @!@!@!@!  !@@!!  @!!!:!{Colors.RESET}")
        time.sleep(0.25)
        print(f"{Colors.RED}!!:      !!: !!:      !!:     !!:     !:!      !!:  !!! !!:  !!!   !!:   !!:  !!! !!:  !!! !!:  !!!     !:! !!:{Colors.RESET}")
        time.sleep(0.25)
        print(f"{Colors.RED} :       :   : ::.: :  :      :   ::.: :       :: :  :   :   : :    :     :   : : :: : ::   :   : : ::.: :  : :: :::{Colors.RESET}")
        useless()
        useless()
        useless()
        useless()
        print(f"{Colors.DIM}Importing FDB...{Colors.RESET}")
        lol2(5)
        useless()
        print(f"{Colors.DIM}Just a random loading bar for suspence and to waste time...{Colors.RESET}")
        lol2(13)
        print(f"{Colors.DIM}W̷e̴l̵c̷o̷m̴e̶...{Colors.RESET}")
        time.sleep(5.5)
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












#print(f"""{Colors.BRIGHT_GREEN}@@@@@@@@ @@@ @@@      @@@@@@@@@@   @@@@@@      @@@@@@@   @@@@@@  @@@@@@@  @@@@@@  @@@@@@@   @@@@@@   @@@@@@ @@@@@@@@
#@@!      @@! @@!      @@! @@! @@! !@@          @@!  @@@ @@!  @@@   @@!   @@!  @@@ @@!  @@@ @@!  @@@ !@@     @@!     
#@!!!:!   !!@ @!!      @!! !!@ @!@  !@@!!       @!@  !@! @!@!@!@!   @!!   @!@!@!@! @!@!@!@  @!@!@!@!  !@@!!  @!!!:!  
#!!:      !!: !!:      !!:     !!:     !:!      !!:  !!! !!:  !!!   !!:   !!:  !!! !!:  !!! !!:  !!!     !:! !!:     
# :       :   : ::.: :  :      :   ::.: :       :: :  :   :   : :    :     :   : : :: : ::   :   : : ::.: :  : :: :::{Colors.RESET}""")
