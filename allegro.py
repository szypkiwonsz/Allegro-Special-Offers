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
        for best_offer in self.get_all_best_offers().find_all('div', {
            'class': '_3kk7b _07bcb_CWOtz _vnd3k _1h8s6 _n1rmb _1t6t8 _m44ca _07bcb_3q-O5'}):
            best_offer_name = best_offer.find('a', {'class': '_1h7wt _15mod _07bcb_2W89U'}).text
            print(best_offer_name)
            best_offer_first_price = best_offer.find('span', {"class": "_swyoj _07bcb_1sAFC"}).text
            best_offer_second_price = best_offer.find('span', {"class": "_1svub _lf05o"}).text
            print(f'{best_offer_first_price} ---> {best_offer_second_price}')

        print('---')

    def category_offers(self):
        other_offersx = self.soup.find('div', {'data-box-name': 'MMO_KONTENER_KATEGORIE'})

        for other_offers in other_offersx.find_all('div', {
            'class': 'opbox-sheet-wrapper _7qjq4 _1yhvf _7ccvy _26e29_2AYAm _9huvz'})[1:]:
            category_name = other_offers.find('h2', {
                'class': 'container-header _1s2v1 _n2pii _35enf _sdhee _9f0v0 _g1a3g _1bwbg _1pelm'})
            print(category_name.text)
            print('---')
            for offer in other_offers.find_all('div', {
                'class': '_3kk7b _07bcb_CWOtz _vnd3k _1h8s6 _n1rmb _1t6t8 _m44ca _07bcb_3q-O5'}):
                offer_name = offer.find('a', {'class': '_1h7wt _15mod _07bcb_2W89U'}).text
                print(offer_name)
                try:
                    offer_first_price = offer.find('span', {"class": "_swyoj _07bcb_1sAFC"}).text
                    offer_second_price = offer.find('span', {"class": "_1svub _lf05o"}).text
                except AttributeError as e:
                    offer_first_price = 'Brak promocji'
                    offer_second_price = 'Nowość!'
                print(f'{offer_first_price} ---> {offer_second_price}')


if __name__ == '__main__':
    source = requests.get('https://allegro.pl/strefaokazji').text

    allegro = Allegro(source)
    allegro.best_offers()
    allegro.category_offers()
