from bs4 import BeautifulSoup
import requests
import re 

# return dict

url = 'https://en.wikipedia.org/wiki/Umbellularia'

r = requests.get(url)

status_code = r.status_code
if status_code != 200 :
    print(f"Problem connecting, status code {status_code}.")
    quit(0)
soup = BeautifulSoup(r.text,"html.parser")

# for i in soup.find_all("td"):
#         for j in i.find_parents('tr'):
#             for k in j.find_parents('tbody'):
#                 for l in k.find_parents('table', class_ ='infobox biota'):
#                     if re.search('Kingdom',i.text):
#                         print(i.text)

char_list = {'Domain':'', 'Kingdom':'', 'Phylum':'', 'Class':'', 'Clade':'', 'Order':'', 
             'Family':'', 'Genus':'', 'Species':''}

for i in soup.find_all('td'):             
    for l in i.find_parents('table', class_ ='infobox biota'):
        for char in char_list.keys():
            if i.text.strip()[0:-1] == char:
                if char == 'Species':
                    char_list[char] = i.find_next('b').text
                elif char == 'Clade':
                    char_list[char] = f"{char_list[char]}{i.find_next('a').text}/"
                else:
                    char_list[char] = i.find_next('a').text
# for i in soup.find('table', class_ ='infobox biota'):
#     infobox_biota = i
print (char_list)

# print(infobox_biota)
# print(type(infobox_biota))
# print(type(soup))