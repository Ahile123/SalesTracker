import requests
from bs4 import BeautifulSoup

class Scraper():
    def __init__(self):
        x = 0

    def get_data(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        list = soup.find_all('a')
        paragraphs = []
        for x in list:
            paragraphs.append(str(x))

        final_List = []
        for seq in paragraphs:
            sub = 'marginright5'
            sub1 = 'plus'
            if seq.find(sub) != -1 and seq.find(sub1) != -1:
                first = seq.find('href=')
                last = seq.find('>') - 1
                final_List.append(seq[first + 6: last])

        for seq in final_List:
            print(seq)