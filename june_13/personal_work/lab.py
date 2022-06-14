import requests
from bs4 import BeautifulSoup
import re

url = "https://butterfly-conservation.org/uk-butterflies/a-to-z"
r = requests.get("https://butterfly-conservation.org/uk-butterflies/a-to-z", verify=False)

soup = BeautifulSoup(r.text, features="html.parser")

links = soup.find_all("a")

# for link in links:
    # print(link.attrs.get('href'))

hrefs = [link.attrs.get('href') for link in links]
# print (hrefs)

butterfly_pages = hrefs[39:100]

# print(butterfly_pages)

urls = ["https://butterfly-conservation.org/" + page for page in butterfly_pages]

# print (urls) 
# We now have a list of urls attached to each butterfly

def get_butterfly(url):
    """Request and parse a single butterfly profile page, return a dict of data."""


    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    h1 = soup.find("h1")
    # print(h1)

    name = h1.text
    # strip() will take off whitespace at the end
    name = name.strip() 
    family = soup.find("li", text = re.compile(r'Family:*'))
    size = soup.find("li", text = re.compile(r'Size:*'))
    wing_span = soup.find("li", text = re.compile(r'Wing Span:*'))
    
   

    return {'name': name,
            'family': peel_data_from_element(family),
            'size': peel_data_from_element(size),
            'wing span': peel_data_from_element(wing_span),
            }

get_butterfly(urls)

def peel_data_from_element(element):
    just_text = element.text
    return just_text.split(': ')[1]

