import os
import sys
import time

class Colors: #Found Parts of List on Stack Overflow
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
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

def slowprint(text, delay=0.015):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

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
    slowprint(Colors.DIM + "Initializing keylog access layer..." + Colors.RESET)
    lol(1.5)
    slowprint(Colors.DIM + "Decrypting logs..." + Colors.RESET)
    lol(1.2)
    slowprint(Colors.GREEN + Colors.BOLD + "ACCESS GRANTED: KEYLOGS STREAM OPEN\n" + Colors.RESET)
Main()