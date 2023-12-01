from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()
fonts = figlet.getFonts()
flag = True

if len(sys.argv) == 1 or len(sys.argv) == 3:
    if len(sys.argv) == 1:
        figlet.setFont(font=choice(fonts))
    else:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
        else:
            flag = False
else:
    flag = False

if not flag:
    sys.exit("Invalid usage")
else:
    print(figlet.renderText(input("Input: ")))