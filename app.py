import requests
from flask import Flask, render_template
from allegro import BestOffers

app = Flask(__name__)


@app.route('/')
def main():
    source = requests.get('https://allegro.pl/strefaokazji').text
    best_offers = BestOffers(source)
    best_offers = best_offers.best_offers()
    return render_template('index.html', **locals())


if __name__ == '__main__':

    app.run()
