from Scraper import Scraper


if __name__ == '__main__':
    URLs = '/Users/sda/Documents/SalesTracker/URLs'
    filter_list = ['iphone', 'plus']
    Current_List = '/Users/sda/Documents/SalesTracker/Current_List'
    with open(URLs, 'r') as f:
        url_list = [line[:-1] for line in f]

    while True:
        scraper = Scraper()
        for url in url_list:
            scraper.get_data(url, Current_List, filter_list)