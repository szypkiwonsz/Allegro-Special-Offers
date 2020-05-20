from bs4 import BeautifulSoup
import requests


class Allegro:

    def __init__(self, site):
        self.site = site
        self.soup = self.get_all_html()

    def get_all_html(self):
        return BeautifulSoup(self.site, 'lxml')

    def get_all_best_offers(self):
        return self.soup.find('div', {"data-box-name": "MMO_ADVERT"})

    def best_offers(self):
        print('MEGA OFERTY')
        print('---')
        for best_offers in self.get_all_best_offers().find_all('div', {
            'class': '_3kk7b _07bcb_CWOtz _vnd3k _1h8s6 _n1rmb _1t6t8 _m44ca _07bcb_3q-O5'}):
            best_offers_name = best_offers.find('a', {'class': '_1h7wt _15mod _07bcb_2W89U'}).text
            print(best_offers_name)
            best_offers_first_price = best_offers.find('span', {"class": "_swyoj _07bcb_1sAFC"}).text
            best_offers_second_price = best_offers.find('span', {"class": "_1svub _lf05o"}).text
            print(f'{best_offers_first_price} ---> {best_offers_second_price}')
        print('---')


if __name__ == '__main__':
    source = requests.get('https://allegro.pl/strefaokazji').text

    allegro = Allegro(source)
    allegro.best_offers()
