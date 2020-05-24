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

    def best_offers_html(self):
        best_offers_all_html = self.soup.find('div', {'data-box-name': 'MMO_ADVERT'})
        best_offers_html = best_offers_all_html.find_all('div', {
            'class': '_3kk7b _07bcb_CWOtz _vnd3k _1h8s6 _n1rmb _1t6t8 _m44ca _07bcb_3q-O5'})
        return best_offers_html

    def get_best_offer_value(self, html_char, attribute):
        offer_list = []
        for best_offer in self.best_offers_products:
            best_offer_value = best_offer.find(html_char, attribute).text
            offer_list.append(best_offer_value)
        return offer_list

    def get_best_offer_image(self, html_char, attribute):
        offer_list = []
        for best_offer in self.best_offers_products:
            best_offer_value = best_offer.find(html_char, attribute).img['data-src']
            offer_list.append(best_offer_value)
        return offer_list

    def get_best_offers_names(self):
        return self.get_best_offer_value('a', {'class': '_1h7wt _15mod _07bcb_2W89U'})

    def get_best_offers_first_price(self):
        return self.get_best_offer_value('span', {'class': '_swyoj _07bcb_1sAFC'})

    def get_best_offers_second_price(self):
        return self.get_best_offer_value('span', {'class': '_1svub _lf05o'})

    def get_best_offers_image(self):
        return self.get_best_offer_image('div', {'class': '_mitvy _qdoeh _1rcax _l7nkx _nyhhx _r6475 _7qjq4'})

    @staticmethod
    def price_to_float(price):
        price = price.replace(',', '.')
        price = price.replace(' ', '')
        price = price[:-3]
        return float(price)

    def percentage(self, first_price, second_price):
        first_price = self.price_to_float(first_price)
        second_price = self.price_to_float(second_price)
        difference = first_price - second_price
        x = 100 * difference // first_price
        return int(x)

    @staticmethod
    def capitalize_offer_name(offers_names):
        capitalized_offers_names = [x.title() for x in offers_names]
        return capitalized_offers_names

    def best_offers(self):
        percentage_list = []
        best_offers_images = self.get_best_offers_image()
        best_offers_names = self.get_best_offers_names()
        best_offers_names = self.capitalize_offer_name(best_offers_names)
        best_offers_first_price = self.get_best_offers_first_price()
        best_offers_second_price = self.get_best_offers_second_price()
        for first_price, second_price in zip(best_offers_first_price, best_offers_second_price):
            x = self.percentage(first_price, second_price)
            percentage_list.append(str(x) + '%')
        return zip(best_offers_images, best_offers_names, best_offers_first_price, best_offers_second_price, percentage_list)
