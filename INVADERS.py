from Colors import Colors

#colors used for Invaders for future use...
#PINK_INVADER = '\033[38;2;209;48;138m'
#YELLOW_INVADER = '\033[38;2;251;224;76m'
#ORANGE_INVADER = '\033[38;2;239;126;49m'
#BLUE_INVADER = '\033[38;2;57;140;209m'
#RED_INVADER = '\033[38;2;75;166;86m'

def really():
    red = [
    f"""{Colors.RED_INVADER}       ▄▄       {Colors.RESET}""",
    f"""{Colors.RED_INVADER}     ▄████▄     {Colors.RESET}""",
    f"""{Colors.RED_INVADER}    ██▄██▄██    {Colors.RESET}""",
    f"""{Colors.RED_INVADER}    ▄▀ ▀▀ ▀▄    {Colors.RESET}""",
    f"""{Colors.RED_INVADER}     ▀    ▀     {Colors.RESET}"""
    ]

    yellow = [
    f"""{Colors.YELLOW_INVADER}     ▀▄   ▄▀      {Colors.RESET}""",
    f"""{Colors.YELLOW_INVADER}    ▄█▀███▀█▄     {Colors.RESET}""",
    f"""{Colors.YELLOW_INVADER}   █▀███████▀█    {Colors.RESET}""",
    f"""{Colors.YELLOW_INVADER}   ▀ ▀▄▄ ▄▄▀ ▀    {Colors.RESET}""",
    f"""{Colors.YELLOW_INVADER}                  {Colors.RESET}"""
    ]

    orange = [
    f"""{Colors.ORANGE_INVADER}      ▄██▄       {Colors.RESET}""",
    f"""{Colors.ORANGE_INVADER}    ▄█▀██▀█▄     {Colors.RESET}""",
    f"""{Colors.ORANGE_INVADER}    ▀▀█▀▀█▀▀     {Colors.RESET}""",
    f"""{Colors.ORANGE_INVADER}    ▄▀▄▀▀▄▀▄     {Colors.RESET}""",
    f"""{Colors.ORANGE_INVADER}                 {Colors.RESET}"""
    ]

    pink = [
    f"""{Colors.PINK_INVADER}   ▄ ▀▄   ▄▀ ▄   {Colors.RESET}""",
    f"""{Colors.PINK_INVADER}   █▄█▀███▀█▄█   {Colors.RESET}""",
    f"""{Colors.PINK_INVADER}   ▀█████████▀   {Colors.RESET}""",
    f"""{Colors.PINK_INVADER}    ▄▀     ▀▄    {Colors.RESET}""",
    f"""{Colors.PINK_INVADER}                 {Colors.RESET}"""
    ]

    blue = [
    f"""{Colors.BLUE_INVADER}    ▄▄███▄▄     {Colors.RESET}""",
    f"""{Colors.BLUE_INVADER}   ██▀▀█▀▀██    {Colors.RESET}""",
    f"""{Colors.BLUE_INVADER}   ▀▀▀█▀█▀▀▀    {Colors.RESET}""",
    f"""{Colors.BLUE_INVADER}    ▄▀ ▀ ▀▄     {Colors.RESET}""",
    f"""{Colors.BLUE_INVADER}                {Colors.RESET}"""
    ]

    for r, y, o, p, b in zip(red, yellow, orange, pink, blue):
        print(y + o + p + b + r)

really()