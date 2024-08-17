import pyfiglet
import sys

if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid Usage")
    
    if sys.argv[2] not in pyfiglet.FigletFont.getFonts():
         sys.exit("Invalid Usage")
    
    result = pyfiglet.figlet_format(input("Input: "), font = f"{sys.argv[2]}")
    print(result)

elif len(sys.argv) == 1:
    result = pyfiglet.figlet_format(input("Input: "))
    print(result)

else:
    sys.exit("Invalid Usage")
