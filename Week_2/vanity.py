#https://cs50.harvard.edu/python/psets/2/plates/

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    if s.isalnum() and 2 <= len(s) <= 6:
        if s[:2].isalpha():
            letters = ''
            numbers = ''
            for n in s:
                if n.isalpha():
                    letters += n
                else:
                    numbers += n
            if len(numbers) > 0:
                if numbers[0] == "0":
                    return False
        
            if s == letters + numbers:
                return True

    return False
    

if __name__ == "__main__":
    main()

