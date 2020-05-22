from bs4 import BeautifulSoup


class Allegro:

    def __init__(self, site):
        self.site = site
        self.soup = self.get_all_html()

    def get_all_html(self):
        return BeautifulSoup(self.site, 'lxml')


class BestOffers(Allegro):

    def __init__(self, site):
        super().__init__(site)
        self.best_offers_products = self.best_offers_html()
        self.best_offers_names = []
        self.best_offers_first_price = []

    def best_offers_html(self):
        best_offers_all_html = self.soup.find('div', {"data-box-name": "MMO_ADVERT"})
        best_offers_html = best_offers_all_html.find_all('div', {
            'class': '_3kk7b _07bcb_CWOtz _vnd3k _1h8s6 _n1rmb _1t6t8 _m44ca _07bcb_3q-O5'})
        return best_offers_html

    def get_best_offers_names(self):
        for best_offer in self.best_offers_products:
            best_offer_name = best_offer.find('a', {'class': '_1h7wt _15mod _07bcb_2W89U'}).text
            self.best_offers_names.append(best_offer_name)
        return self.best_offers_names

    def get_best_offers_first_price(self):
        for best_offer in self.best_offers_products:
            best_offer_first_price = best_offer.find('span', {"class": "_swyoj _07bcb_1sAFC"}).text
            self.best_offers_first_price.append(best_offer_first_price)
        return self.best_offers_first_price

    def best_offers(self):
        return zip(self.get_best_offers_names(), self.get_best_offers_first_price())



    # def best_offers(self):
    #     best_offers = []
    #     for best_offer in self.get_all_best_offers().find_all('div', {
    #         'class': '_3kk7b _07bcb_CWOtz _vnd3k _1h8s6 _n1rmb _1t6t8 _m44ca _07bcb_3q-O5'}):
    #         best_offer_name = best_offer.find('a', {'class': '_1h7wt _15mod _07bcb_2W89U'}).text
    #         best_offers.append(best_offer_name)
    #         best_offer_first_price = best_offer.find('span', {"class": "_swyoj _07bcb_1sAFC"}).text
    #         best_offer_second_price = best_offer.find('span', {"class": "_1svub _lf05o"}).text
    #     return best_offers

    # def category_offers(self):
    #     other_offersx = self.soup.find('div', {'data-box-name': 'MMO_KONTENER_KATEGORIE'})
    #
    #     for other_offers in other_offersx.find_all('div', {
    #         'class': 'opbox-sheet-wrapper _7qjq4 _1yhvf _7ccvy _26e29_2AYAm _9huvz'})[1:]:
    #         category_name = other_offers.find('h2', {
    #             'class': 'container-header _1s2v1 _n2pii _35enf _sdhee _9f0v0 _g1a3g _1bwbg _1pelm'})
    #         print(category_name.text)
    #         print('---')
    #         for offer in other_offers.find_all('div', {
    #             'class': '_3kk7b _07bcb_CWOtz _vnd3k _1h8s6 _n1rmb _1t6t8 _m44ca _07bcb_3q-O5'}):
    #             offer_name = offer.find('a', {'class': '_1h7wt _15mod _07bcb_2W89U'}).text
    #             print(offer_name)
    #             try:
    #                 offer_first_price = offer.find('span', {"class": "_swyoj _07bcb_1sAFC"}).text
    #                 offer_second_price = offer.find('span', {"class": "_1svub _lf05o"}).text
    #             except AttributeError as e:
    #                 offer_first_price = 'Brak promocji'
    #                 offer_second_price = 'Nowość!'
    #             print(f'{offer_first_price} ---> {offer_second_price}')
