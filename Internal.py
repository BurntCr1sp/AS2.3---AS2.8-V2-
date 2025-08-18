import sqlite3
from Colors import Colors
import time
import sys
import os

DATABASE = 'database.db'

def useless(number):
    for _ in range(number):
        print('')

def loading_bar2(duration=2, width=114):
    sys.stdout.write(Colors.CYAN + "[")
    for _ in range(width):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(duration / width)
    sys.stdout.write("]" + Colors.RESET + "\n")

def Database_format(Films):
    id_, name, year, rating, length, genre = [str(f or '') for f in Films]
    header = f'{Colors.RED}ID:{id_:<4}{Colors.RESET} {Colors.BRIGHT_YELLOW}YEAR:{year:<7} RATING:{rating}{Colors.RESET}\n'
    container1 = f'{Colors.BRIGHT_YELLOW}-- NAME --{Colors.RESET}\n{name}\n'
    container2 = f'{Colors.BRIGHT_YELLOW}-- LENGTH --{Colors.RESET}\n{length}\n'
    container3 = f'{Colors.BRIGHT_YELLOW}-- GENRE --{Colors.RESET}\n{genre}\n'
    connect = f"{header}\n{container1}\n{container2}\n{container3}\n" + "-"*70
    return connect

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
        loading_bar2(3)
        useless(1)
        print(f"{Colors.DIM}Just a random loading bar for suspence and to waste time...{Colors.RESET}")
        loading_bar2(3)
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
        useless(4)

        cursor.execute(select_query)
        data1 = cursor.fetchall()
        
        for data in data1:
            print(Database_format(data))

def addtoDB(DATABASE, name, year, rating, length, genre):
    try:
        connect = sqlite3.connect(DATABASE)
        cursor = connect.cursor()
        print("Attempting to insert:", name, year, rating, length, genre)
        cursor.execute(
            "INSERT INTO \"Films\" (Name, Year, Rating, Length, Genre) VALUES (?, ?, ?, ?, ?)", 
            (name, year, rating, length, genre)
        )
        connect.commit()
        return "Film added successfully."
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
    finally:
        if connect:
            connect.close()

def searchDB():
    ...

def exportDB():
    ...










#print(f"""{Colors.BRIGHT_GREEN}@@@@@@@@ @@@ @@@      @@@@@@@@@@   @@@@@@      @@@@@@@   @@@@@@  @@@@@@@  @@@@@@  @@@@@@@   @@@@@@   @@@@@@ @@@@@@@@
#@@!      @@! @@!      @@! @@! @@! !@@          @@!  @@@ @@!  @@@   @@!   @@!  @@@ @@!  @@@ @@!  @@@ !@@     @@!     
#@!!!:!   !!@ @!!      @!! !!@ @!@  !@@!!       @!@  !@! @!@!@!@!   @!!   @!@!@!@! @!@!@!@  @!@!@!@!  !@@!!  @!!!:!  
#!!:      !!: !!:      !!:     !!:     !:!      !!:  !!! !!:  !!!   !!:   !!:  !!! !!:  !!! !!:  !!!     !:! !!:     
# :       :   : ::.: :  :      :   ::.: :       :: :  :   :   : :    :     :   : : :: : ::   :   : : ::.: :  : :: :::{Colors.RESET}""")
