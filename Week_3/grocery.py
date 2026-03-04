#https://cs50.harvard.edu/python/psets/3/grocery/


def main():
    grocery_list = {}
    
    while True:
        try:
            user_input = input().strip().upper()
            grocery_list[user_input] = grocery_list.get(user_input, 0) + 1
        except EOFError:
            break
        
    for item in sorted(grocery_list):
        print(grocery_list[item], item)
            
        
if __name__ == "__main__":
    main()
