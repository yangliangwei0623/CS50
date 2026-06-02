import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
if len(sys.argv) == 1:
    str = input("INPUT: ")
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(str))
elif len(sys.argv) == 3 and sys.argv[1] == "-f":
    str = input("INPUT: ")
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        sys.exit("Invalid font")
    print(figlet.renderText(str))
else:   
    sys.exit("Invalid usage")
