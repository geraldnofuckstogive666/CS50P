def main():
    user_input =input()
    print(convert(user_input))




def convert(s):
    new_string = ""
    for word in s.split():
        if word == ":)":
            new_string += "🙂 "
        elif word == ":(":
            new_string += "🙁 "
        else:
            new_string += word + " "

    return new_string.strip()

if __name__ == "__main__":
    main()