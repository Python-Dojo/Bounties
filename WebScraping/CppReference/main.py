import requests
from bs4 import BeautifulSoup

url = 'https://en.cppreference.com/w/cpp/algorithm/ranges/for_each'
html = requests.get(url)

#print the Algorithm page in html format
# print(html.text)

soup = BeautifulSoup(html.content, 'html.parser')
# print(soup.prettify())

function_type = soup.find('span', class_ = 'kw4')
print(function_type.text)

function = soup.find_all(class_='mw-geshi cpp source-cpp')
# print(function[0].text)

# Find and exclude the <span> element with class 'kw4'
kw4_element = function[0].find('span', class_='kw4')
if kw4_element:
    kw4_element.decompose()

# Access and print the modified text content of the <span> element
print(function[0].text.strip())


# Find and exclude the <span> element with class 'kw4'
kw4_element_2 = function[1].find('span', class_='kw4')
if kw4_element_2:
    kw4_element_2.decompose()

print(function[1].text.strip())

function_description = soup.find(class_= 't-li1')
print(function_description.text)

# Find the <div> tag with class 't-li1'
div_tag = soup.find('div', class_='t-li1')

# Find the <p> tag that is a sibling of the <div> tag
p_tag = div_tag.find_next_sibling('p')

# Print the text content of the <p> tag
if p_tag:
    print('TEST:',p_tag.text.strip())
else:
    print("Sibling <p> tag not found.")