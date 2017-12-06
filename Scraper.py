import requests
from bs4 import BeautifulSoup
from Send_Mail import Send_Mail

class Scraper():
    def __init__(self):
        x = 0

    def read_list(self, Current_List):
        with open(Current_List, 'r') as f:
            listWords = [line[:-1] for line in f]

        #print (listWords)

    def get_data(self, url, Current_List):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        list = soup.find_all('a')
        paragraphs = []
        for x in list:
            paragraphs.append(str(x))

        final_List = []
        for seq in paragraphs:
            sub1 = 'marginright5'
            sub2 = 'plus'
            sub3 = 'iphone'
            if seq.find(sub1) != -1 and seq.find(sub2) != -1 and seq.find(sub3) != -1:
                first = seq.find('href=')
                last = seq.find('>') - 1
                final_List.append(seq[first + 6: last])

        with open(Current_List, 'r') as f:
            listWords = [line[:-1] for line in f]

        send = Send_Mail()
        for seq in final_List:
            if not seq in listWords:
                send.send_mail('ahile.scraper', 'ahile123', 'echipa.lion@gmail.com', seq, seq)
                listWords.append(seq)

        myFile = open(Current_List, 'w')
        for word in listWords:
            print(word, file=myFile)
        '''for seq in final_List:
            print(seq)'''
