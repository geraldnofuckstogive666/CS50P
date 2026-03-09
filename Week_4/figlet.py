#https://cs50.harvard.edu/python/psets/4/figlet/
#need: pip install pyfiglet

import sys
import random
import pyfiglet 


def main():
    fonts = pyfiglet.Figlet().getFonts()

    if len(sys.argv) == 1:
        user_input = input("Input: ")
        f = random.choice(fonts)
    
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ("-f",  "--font"):
            sys.exit("Invalid usage")
        
        if sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        
        user_input = input("Input: ")
        f = sys.argv[2]

    else: 
        sys.exit("Invalid usage")


    print(f"Output:\n{pyfiglet.figlet_format(user_input, f)}")


if __name__ == "__main__":
    main()