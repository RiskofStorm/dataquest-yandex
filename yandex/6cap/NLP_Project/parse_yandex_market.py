# import pickle
# from multiprocessing import Pool
# import time
# import random
# import requests
# import bs4

# def parse_page(url):
#     time.sleep(random.randint(5,30))
    
#     text = requests.get(url)
#     text.encoding = "utf-8"
    
#     parser = bs4.BeautifulSoup(text.text, 'lxml')
#     data = parser.findAll('div', attrs={"class":"n-snippet-card-review__right"})
    
#     full_revs = [" ".join([t.text for t in i.find_all('dd')]) for i in data]

#     rating_revs = [1 if float(i.text) > 3 else 0  for i in 
#                    parser.findAll('div', attrs={'class':'rating__value'})]
    
#     return list(zip(full_revs, rating_revs))

# url = """https://market.yandex.ru/catalog--mobilnye-telefony-otzyvy-pokupatelei/54726/list?\
# show-reviews=1&page={}&local-offers-first=0&onstock=0&how=quality"""

# pool = Pool(3)
# url_list = [url.format(i) for i in range(2,51)]
# url_list_2 = [url.format(i) for i in range(52,151)]
# if __name__ == "__main__":
#     map_results = pool.map(parse_page, url_list)
#     with open('parsing_revievs_yandexMarket','wb') as out_f:
#         pickle.dump(map_results, out_f)
