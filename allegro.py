from bs4 import BeautifulSoup
import requests

source = requests.get('https://allegro.pl/strefaokazji').text

soup = BeautifulSoup(source, 'lxml')
