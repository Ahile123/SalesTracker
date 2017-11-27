from Scraper import Scraper

URL1 = 'https://www.olx.ro/bucuresti/q-iphone-7-plus-neactivat/?search%5Bdescription%5D=1&search%5Bfilter_float_price%3Afrom%5D=2100&search%5Bfilter_float_price%3Ato%5D=2550&search%5Bdist%5D=15'
URL2 = 'https://www.olx.ro/bucuresti/q-iphone-7-plus-sigilat/?search%5Bdescription%5D=1&search%5Bfilter_float_price%3Afrom%5D=2100&search%5Bfilter_float_price%3Ato%5D=2550&search%5Bdist%5D=15'

if __name__ == '__main__':
    scraper = Scraper()
    scraper.get_data(URL1)
    #scraper.get_data(URL2)
