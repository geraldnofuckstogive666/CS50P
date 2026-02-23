#https://cs50.harvard.edu/python/psets/2/coke/

denominations = (5, 10, 25)

def main():
    due = 50

    while due > 0:
        print(f"Amount Due: {due}")
        
        try:
            coin = int(input("Insert coin: "))
        except ValueError:
            continue

        if coin in denominations:
            due -= coin

    print(f"Change owed: {abs(due)}")
        

if __name__ == "__main__":
    main()