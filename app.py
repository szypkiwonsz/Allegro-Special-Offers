import requests
from flask import Flask, render_template
from allegro import BestOffers

app = Flask(__name__)


@app.route('/')
def main():
    source = requests.get('https://allegro.pl/strefaokazji').text
    best_offers_products = BestOffers(source)
    best_offers_sorted = sorted(best_offers_products.best_offers(), key=lambda x: int((x[4]).replace('%', '')),
                                reverse=True)
    return render_template('index.html', **locals())


if __name__ == '__main__':

    app.run()
