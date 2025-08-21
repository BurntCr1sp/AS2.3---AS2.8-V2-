import time, random, os

def error():
    text = "[!!] ✖ ERROR ✖ [!!]"
    ascii = "█▓▒░#@%&$"
    colors = [
    '\033[0m',
    '\033[30m',
    '\033[31m',
    '\033[32m',
    '\033[33m',
    '\033[34m',
    '\033[38;5;208m',
    '\033[35m',
    '\033[36m',
    '\033[37m',
    '\033[90m',
    '\033[91m',
    '\033[92m',
    '\033[93m',
    '\033[94m',
    '\033[95m',
    '\033[96m',
    '\033[97m',
    '\033[38;2;209;48;138m',
    '\033[38;2;251;224;76m',
    '\033[38;2;239;126;49m',
    '\033[38;2;57;140;209m',
    '\033[38;2;75;166;86m'
]


    for _ in range(25):
        os.system('cls' if os.name == 'nt' else 'clear')
        color = random.choice(colors)
        offset = " " * random.randint(0, 3)
        glitch = ''.join(c if random.random() > 0.1 else random.choice(ascii) for c in text)
        print(f"{color}{offset}{glitch}\033[0m")
        time.sleep(0.1)

error()