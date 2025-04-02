from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_trees_and_shrubs_by_taxonomic_family'

def tree_page_scraper(url) -> list:

    r = requests.get(url)

    status_code = r.status_code
    if status_code != 200 :
        print(f"Problem connecting, status code {status_code}.")
        quit(0)

    soup = BeautifulSoup(r.text,"html.parser")

    tree_links = []

    for i in soup.find_all("a"):
        for j in i.find_parents('i'):
            for k in j.find_parents('td'):
                for l in k.find_parents('tr'):
                    tree_links.append(f"https://en.wikipedia.org{i.get('href')}")

    # Remove duplicates
    tree_links=list(set(tree_links))

    return tree_links