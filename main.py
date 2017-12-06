from Scraper import Scraper

URL7ne= 'https://www.olx.ro/bucuresti/q-iphone-7-plus-neactivat/?search%5Bdescription%5D=1&search%5Bfilter_float_price%3Afrom%5D=2100&search%5Bfilter_float_price%3Ato%5D=2450&search%5Bdist%5D=15'
URL7si = 'https://www.olx.ro/bucuresti/q-iphone-7-plus-sigilat/?search%5Bdescription%5D=1&search%5Bfilter_float_price%3Afrom%5D=2100&search%5Bfilter_float_price%3Ato%5D=2450&search%5Bdist%5D=15'

URL6ne = 'https://www.olx.ro/oferte/q-iphone-6s-plus-neactivat/?search%5Bdescription%5D=1&search%5Bfilter_float_price%3Afrom%5D=1500&search%5Bfilter_float_price%3Ato%5D=1850'
URL6si = 'https://www.olx.ro/oferte/q-iphone-6s-plus-sigilat/?search%5Bdescription%5D=1&search%5Bfilter_float_price%3Afrom%5D=1500&search%5Bfilter_float_price%3Ato%5D=1850'

if __name__ == '__main__':
    while True:
        scraper = Scraper()
        scraper.get_data(URL7ne, Current_List='/Users/sda/Documents/SalesTracker/Current_List')
        scraper.get_data(URL7si, Current_List='/Users/sda/Documents/SalesTracker/Current_List')
        scraper.get_data(URL6ne, Current_List='/Users/sda/Documents/SalesTracker/Current_List')
        scraper.get_data(URL6si, Current_List='/Users/sda/Documents/SalesTracker/Current_List')