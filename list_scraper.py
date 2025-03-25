from bs4 import BeautifulSoup
import requests

r = requests.get('https://en.wikipedia.org/wiki/List_of_trees_and_shrubs_by_taxonomic_family')

status_code = r.status_code
if status_code != 200 :
    print(f"Problem connecting, status code {status_code}.")
    quit(0)

soup = BeautifulSoup(r.text,"html.parser")

tree_links = []
# for tree in soup.find_all("a",class_ = "mw-redirect"):
#     tree_links.append("https://en.wikipedia.org{tree.get('href')}")

# print(tree_links)
# print(len(tree_links))

for i in soup.find_all("a"):
    for j in i.find_parents('i'):
        for k in j.find_parents('td'):
            for l in k.find_parents('tr'):
                tree_links.append(f"https://en.wikipedia.org{i.get('href')}")

tree_links=list(set(tree_links))
for i in range(0,12):
    print(tree_links[i])
print(len(tree_links))
