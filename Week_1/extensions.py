#https://cs50.harvard.edu/python/psets/1/extensions/
import requests
from bs4 import BeautifulSoup

URLz = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types"

def get_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_extensions(html_text: str) -> dict:
    if not html_text:
        return {}
    
    soup = BeautifulSoup(html_text,'html.parser')
    rows = soup.find_all('tr')
    extensions = {}
    for row in rows:
        cols = row.find_all('td')   
        
        if len(cols) == 3:          
            extension_text = cols[0].get_text(strip=True)
            mime_text = cols[2].get_text(strip=True)
            mime = (mime_text.split())[0]



            extension_list = extension_text.split(",")
            for ext in extension_list:
                extension = ext.strip()
                extensions[extension] = mime
    return extensions


def get_mime_type(extensions: dict, filename: str) -> str:
    if "." not in filename:
        return "application/octet-stream"

    ext = "." + filename.lower().split(".")[-1]
    return extensions.get(ext, "application/octet-stream")


def main():
    html_text = get_data(URLz)
    extensions = parse_extensions(html_text)
    user_file = input("File name: ").lower().strip()
    print(get_mime_type(extensions, user_file))


if __name__ == "__main__":
    main()