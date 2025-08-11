import time, random, os

def error():
    text = "[!!] ✖ ERROR ✖ [!!]"
    chars = "█▓▒░#@%&$"
    colors = ["\033[91m", "\033[93m", "\033[97m", "\033[95m"]

    for _ in range(25):
        os.system('cls' if os.name == 'nt' else 'clear')
        color = random.choice(colors)
        offset = " " * random.randint(0, 3)
        glitch = ''.join(c if random.random() > 0.1 else random.choice(chars) for c in text)
        print(f"{color}{offset}{glitch}\033[0m")
        time.sleep(0.1)
