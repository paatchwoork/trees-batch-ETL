from bs4 import BeautifulSoup
import requests
import re 

# return dict

url = 'https://en.wikipedia.org/wiki/Sequoia_sempervirens'#'https://en.wikipedia.org/wiki/Umbellularia'

def page_scraper(url)->dict :

    print(f"Connecting to {url}")

    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
            print("Connection error !")
    finally:
        r = requests.get(url)

    status_code = r.status_code
    if status_code != 200 :
        print(f"Problem connecting to url {url}, status code {status_code}.")
        return {}
    else:
        print("Connection successful")
    
    soup = BeautifulSoup(r.text,"html.parser")

    char_list = {'Domain':'Eukarya', 'Kingdom':'', 'Phylum':'', 'Class':'', 'Clade':'', 'Order':'', 
                'Family':'', 'Genus':'', 'Species':'', 'Conservation status': '', 'Names': ''}

    for i in soup.find_all('td'):             
        for l in i.find_parents('table', class_ ='infobox biota'):
            for char in char_list.keys():
                if i.text.strip()[0:-1] == char:
                    # if char == 'Species':
                    #     char_list[char] = i.find_next('b').text
                    if char == 'Clade':
                        char_list[char] = f"{char_list[char]}{i.find_next('a').text}/"
                    else:
                        char_list[char] = i.find_next('a').text

    for i in soup.find_all('a'):             
        for l in i.find_parents('table', class_ ='infobox biota'):
            if i.text == 'Conservation status':
                char_list['Conservation status'] = i.find_next('a').text

    first = True
    for i in soup.find_all('b'):             
        for l in i.find_parents('p'):
            if first:
                char_list['Species'] = i.text
                first = False
            else:
                char_list['Names'] = f"{char_list['Names']}{i.text}/"


    return char_list