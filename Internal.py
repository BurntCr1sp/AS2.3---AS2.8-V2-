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

def Database_format(Films):
    id_, name, year, rating, length, genre = [str(f or '') for f in Films]
    header = f'ID:{id_:<4} YEAR:{year} RATING:{rating}'
    container1 = f'-- NAME --\n{name}'
    container2 = f'-- LENGTH --\n{length}'
    container3 = f'-- GENRE --\n{genre}'
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
        useless(4)

        cursor.execute(select_query)
        data1 = cursor.fetchall()
        
        for data in data1:
            print(Database_format(data))

def addtoDB(DATABASE, Name, Year, Rating, Length, Genre):
    try:
        connect = sqlite3.connect(DATABASE)
        cursor = connect.cursor()
        print("Attempting to insert:", Name, Year, Rating, Length, Genre)
        cursor.execute(
            "INSERT INTO \"Films\" (Name, Year, Rating, Length, Genre) VALUES (?, ?, ?, ?, ?)", 
            (Name, Year, Rating, Length, Genre)
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
