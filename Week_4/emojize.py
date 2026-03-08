#https://cs50.harvard.edu/python/psets/4/emojize/
#need to run: pip install emoji    

import emoji



def main():
    user_input = input("Input: ").strip()
    output = emoji.emojize(user_input, language='alias')
    print(f"Output: {output}")


if __name__ == "__main__":
    main()