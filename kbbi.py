# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import sys

base_url = 'http://kbbi4.portalbahasa.com'

def cari(teks):
    r = requests.get('{}/entri/{}'.format(base_url, teks))
    soup = BeautifulSoup(r.text, 'html.parser')
    entries = []
    for elm in soup.find_all('span', {'class': 'syllable'}):
        lafal = elm.text
        deskripsi = []
        for child in elm.parent.find_next_sibling('ol').find_all('li'):
            atribut = []
            for e in child.find_all('a', {'class': 'attribute'}):
                atribut.append(e['title'])
                e.decompose()
            for e in child.find_all('span', {'title': lambda x: x}):
                atribut.append(e['title'])
                e.decompose()
            contoh = []
            for e in child.find_all('span', {'class': 'sample'}):
                contoh.append(e.text)
                e.decompose()
            latin = ''
            if child.find('span', {'class': 'latin'}):
                latin = child.find('span', {'class': 'latin'}).text
                child.find('span', {'class': 'latin'}).decompose()
            arti = child.text.strip()
            deskripsi.append({'atribut': atribut, 'arti': arti, 'latin': latin, 'contoh': contoh})
        entries.append({'lafal': lafal, 'deskripsi': deskripsi})
    return entries

def main():
    print(json.dumps(cari(sys.argv[1]), indent=4))

if __name__ == '__main__':
    main()