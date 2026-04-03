#https://cs50.harvard.edu/python/psets/7/watch/

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if s := re.search(r".+?src=\"https?://(?:www.)?youtube\.com/embed/([a-z0-9]+)\".+?",s,flags=re.IGNORECASE):
        url = s.group(1)
        return f"https://youtu.be/{url}"
    else:
        return None




if __name__ == "__main__":
    main()