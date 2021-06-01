#print("Web Scraping")

# If you want to scrape a website:

# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4

# Step 0 :--

# some important library used in Web Scraping
# pip install requests
# pip install bs4
# pip install html5lib
import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com"

# step 1 : Get the HTML

r = requests.get(url)

html_Contnt = r.content

# print(html_Contnt)


# step 2 : parse the HTML

soup = BeautifulSoup(html_Contnt, 'html.parser')
# print(soup.prettify)

# step 3 : HTML Tree traversal

# Get the title of html page

title = soup.title
# commonly used types of objects:

# print(type(title))  # 1. Tag
# print(type(title.string))  # 2. NavigableString
# print(type(soup))  # 3. BeautifulSoup
# 4. Comment


# print(title)
