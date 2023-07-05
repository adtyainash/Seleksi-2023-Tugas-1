# import requests
# from bs4 import BeautifulSoup
 
# url = 'https://reviews.femaledaily.com/products/lips/lipstick?brand=&order=popular&page=1'
# # headers = {
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
# # }
# req = requests.get(url)
# soup = BeautifulSoup(req.text, 'html.parser')
# items = soup.findAll('div', 'jsx-2856971448 product-item')
# print(items)
# for it in items:
#     name = it.find('h2', 'jsx-2059197805 product-card-catalog-title').text
#     print(name)

import requests
from bs4 import BeautifulSoup
import csv
 
key = input('please enter the term :')
location = input('please enter the location too :')
url = 'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=1673388186&keywords={}&location={}&pageNum='.format(key, location)
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
 
datas = []
count_page = 0
for page in range(1, 11):
    count_page+=1
    print('scraping page :',count_page)
    req = requests.get(url+str(page), headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    items = soup.findAll('div', 'row businessCapsule--mainRow')
    for it in items:
        name = it.find('span', 'businessCapsule--name').text
        try : address = ''.join(it.find('span', {'itemprop':'address'}).text.strip().split('\n'))
        except : address = ''
        try : web = it.find('a', {'rel':'nofollow noopener'})['href'].replace('http://', '').replace('www.', '').replace('https://', '').split('/')[0]
        except : web = ''
        try : telp = it.find('span', 'business--telephoneNumber').text
        except: telp= ''
        image = it.find('div', 'col-sm-4 col-md-4 col-lg-5 businessCapsule--leftSide').find('img')['data-original']
        if 'http' not in image: image = 'https://www.yell.com{}'.format(image)
        datas.append([name, address, web, telp, image])
 
kepala = ['Name', 'Address', 'Website', 'Phone Number', 'Image URL']
writer = csv.writer(open('results/{}_{}.csv'.format(key, location), 'w', newline=''))
writer.writerow(kepala)
for d in datas: writer.writerow(d)