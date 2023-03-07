from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# Lets try without submitted forms first

searches = ['peter+infeld+violin+set']

# For thestringzone.co.uk, search : key
stringzone = {}

for search in searches:
    # Initialize Beatiful Soup with GET request
    page = urlopen(f'https://www.thestringzone.co.uk/search?utf8=%E2%9C%93&q={search}')
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    
    # Search for specific price tag
    tag = soup.find(string='Thomastik Peter Infeld Violin Strings, SET')
    price_tag = tag.find_parent().find_parent().find_parent().find(class_="price")
    price = str(price_tag).lstrip('<span class="price">').rstrip('</span>').strip()
    
    # Put in Dict   
    key = search.replace('+', ' ')
    stringzone[key] = price
    

print(stringzone)