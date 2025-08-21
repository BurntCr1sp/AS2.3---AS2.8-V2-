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

def exportDB(Films, filename="FDB_export.txt"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for film in Films:
                id_, name, year, rating, length, genre = [str(f or '') for f in film]

                f.write(f"ID:{id_:<4} YEAR:{year:<7} RATING:{rating}\n")
                f.write("-- NAME --\n")
                f.write(name + "\n")
                f.write("-- LENGTH --\n")
                f.write(length + "\n")
                f.write("-- GENRE --\n")
                f.write(genre + "\n")
                f.write("-" * 50 + "\n")

        print(f"{Colors.BRIGHT_YELLOW}>> Films exported to {filename}{Colors.RESET}")
    except Exception as e:
        print(Colors.RED + f">> Export error: {e}" + Colors.RESET)

def removefromDB(DATABASE, selectedID):
    while True:
        print("Sure, no going back? (y/n):")
        sure = input(f'{Colors.BRIGHT_YELLOW}>>> {Colors.RESET}').lower()
        if sure == 'y':
            try:
                connect = sqlite3.connect(DATABASE)
                cursor = connect.cursor()
                cursor.execute("DELETE FROM \"Films\" WHERE ID = ?", (selectedID,))
                connect.commit()
                print("Card successfully removed")
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
            finally:
                connect.close()
            break
        elif sure == 'n':
            print("Operation cancelled")
            break 
        else:
            print("Invalid input. Please enter 'y' or 'n'.")









#print(f"""{Colors.BRIGHT_GREEN}@@@@@@@@ @@@ @@@      @@@@@@@@@@   @@@@@@      @@@@@@@   @@@@@@  @@@@@@@  @@@@@@  @@@@@@@   @@@@@@   @@@@@@ @@@@@@@@
#@@!      @@! @@!      @@! @@! @@! !@@          @@!  @@@ @@!  @@@   @@!   @@!  @@@ @@!  @@@ @@!  @@@ !@@     @@!     
#@!!!:!   !!@ @!!      @!! !!@ @!@  !@@!!       @!@  !@! @!@!@!@!   @!!   @!@!@!@! @!@!@!@  @!@!@!@!  !@@!!  @!!!:!  
#!!:      !!: !!:      !!:     !!:     !:!      !!:  !!! !!:  !!!   !!:   !!:  !!! !!:  !!! !!:  !!!     !:! !!:     
# :       :   : ::.: :  :      :   ::.: :       :: :  :   :   : :    :     :   : : :: : ::   :   : : ::.: :  : :: :::{Colors.RESET}""")
