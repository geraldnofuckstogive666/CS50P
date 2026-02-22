#https://cs50.harvard.edu/python/psets/1/meal/

def main():
    user_input = input("What time is it? ").strip()
    current_time = convert(user_input)
    
    if 7 <= current_time  <= 8:
        print("breakfast time")
    elif 12 <= current_time  <= 13:
        print("lunch time")
    elif 18 <= current_time  <=19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    h = float(hour)
    m = float(minute) / 60
    return h + m

if __name__ == "__main__":
    main()