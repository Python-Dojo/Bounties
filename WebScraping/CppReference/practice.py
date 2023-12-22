#Vector

import requests
from bs4 import BeautifulSoup

url = 'https://en.cppreference.com/w/cpp/container/vector'
html = requests.get(url)

#print the Algorithm page in html format
# print(html.text)

soup = BeautifulSoup(html.content, 'html.parser')
# print(soup.prettify())

example_class = soup.find(class_='cpp source-cpp')
example = example_class.find('pre')

print(example.text)

function_class = soup.find(class_='t-dcl-begin')
function = function_class.find('tbody')

print(function.text)