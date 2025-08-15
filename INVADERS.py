from Colors import Colors


def really():
    red = [
    f"""{Colors.RED_INVADER}       ▄▄       {Colors.RESET}""",
    f"""{Colors.RED_INVADER}     ▄████▄     {Colors.RESET}""",
    f"""{Colors.RED_INVADER}    ██▄██▄██     {Colors.RESET}""",
    f"""{Colors.RED_INVADER}    ▄▀ ▀▀ ▀▄     {Colors.RESET}""",
    f"""{Colors.RED_INVADER}     ▀    ▀      {Colors.RESET}"""
    ]

    yellow = [
    f"""{Colors.YELLOW_INVADER}     ▀▄    ▄▀     {Colors.RESET}""",
    f"""{Colors.YELLOW_INVADER}    ▄█▀████▀█▄    {Colors.RESET}""",
    f"""{Colors.YELLOW_INVADER}   █▀████████▀█   {Colors.RESET}""",
    f"""{Colors.YELLOW_INVADER}   █ █▀▀▀▀▀▀█ █   {Colors.RESET}""",
    f"""{Colors.YELLOW_INVADER}      ▀▀  ▀▀      {Colors.RESET}"""
    ]

    orange = [
    f"""{Colors.ORANGE_INVADER}      ▄██▄       {Colors.RESET}""",
    f"""{Colors.ORANGE_INVADER}    ▄██████▄     {Colors.RESET}""",
    f"""{Colors.ORANGE_INVADER}   ███▄██▄███    {Colors.RESET}""",
    f"""{Colors.ORANGE_INVADER}     ▄▀▄▄▀▄      {Colors.RESET}""",
    f"""{Colors.ORANGE_INVADER}    ▀ ▀  ▀ ▀     {Colors.RESET}"""
    ]

    pink = [
    f"""{Colors.PINK_INVADER}   ▄ ▀▄    ▄▀ ▄   {Colors.RESET}""",
    f"""{Colors.PINK_INVADER}   █▄████████▄█   {Colors.RESET}""",
    f"""{Colors.PINK_INVADER}   ███▄████▄███   {Colors.RESET}""",
    f"""{Colors.PINK_INVADER}   ▀██████████▀   {Colors.RESET}""",
    f"""{Colors.PINK_INVADER}    ▄▀      ▀▄    {Colors.RESET}"""
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
