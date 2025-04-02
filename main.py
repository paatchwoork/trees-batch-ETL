# import sys
# import os
# sys.path.append(os.path.abspath("./src/"))
from src.list_scraper import tree_page_scraper
from src.page_scraper import page_scraper

from multiprocessing.pool import ThreadPool

url = 'https://en.wikipedia.org/wiki/List_of_trees_and_shrubs_by_taxonomic_family'

trees_list = tree_page_scraper(url)
trees_char_list = []

# print(page_scraper(trees_list[134]))

# for tree in trees_list:
#     # print(tree)
#     trees_char_list.append(page_scraper(tree))
with ThreadPool(5) as pool:
    trees_char_list = pool.map(page_scraper, trees_list, chunksize=10)

for i in range(0,10):
    print(trees_char_list[i])
