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

# Get all the paragraphs from the page

paras = soup.find_all('p')
# print(paras)

# Get all the anchor tag from the page

anchor = soup.find_all('a')
# print(anchor)

# print(soup.find('p'))  # Get first element

# print(soup.find('header')['id'])  # Get Ids of any element

# print(soup.find('p')['class'])  # Get classes of any element

# find all the elements with class lead

#print(soup.find_all('p', class_='lead'))

# find all text data from p tag

# print(soup.find('p').get_text())

#print(soup.find('p', class_='lead').get_text())


# get all the lonks on the HTML page

anchor = soup.find_all('a')
all_links = set()
for link in anchor:
    if(link.get('href') != '#'):
        link_text = 'https://codewithharry.com' + link.get('href')
        all_links.add(link)
      #  print(link_text)


# step 3 : tree_Traversal

# comment

#markup = "<p><!-- this is a comment --></p>"
#soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))
# print((soup2.p.string))
# print(soup2.p)


navbarSupportedContent = soup.find(id='navbarSupportedContent')

# print(navbarSupportedContent.contents)

# for elem in navbarSupportedContent.children:
# print(elem)


# for elem in navbarSupportedContent.contents:
#  print(elem)

# for elem in navbarSupportedContent.strings:
# print(elem)

# for elem in navbarSupportedContent.stripped_strings:
#    print(elem)

# .contents - A tag's children are avaliable as a list (It store in our memory )
# .children - A tag's children are avaliable as a generator (but it is just itrating item )

# print(navbarSupportedContent.parent)

# print(navbarSupportedContent.parents)

# for item in navbarSupportedContent.parents:
#    print(item.name)


# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

elem = soup.select('#loginModal')
print(elem)
