from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re

l_rajonas = []
l_gatve = []
l_kaina = []
l_kvadratas = []
l_kambariai = []
l_plotas = []
l_aukstas = []
l_aukstu = []

##########################################
# Pirmas Puslapis parduodamu butu

url = 'https://www.aruodas.lt/butai/vilniuje/'
page = requests.get(url, allow_redirects=False)
soup = bs(page.content, 'html.parser')
elems = soup.find_all('tr', class_='list-row')
for elem in elems:
    try:
        rajonas = elem.find(
            'td', class_='list-adress').h3.get_text('/').split('/')[1]
        gatve = elem.find(
            'td', class_='list-adress').h3.get_text('/').split('/')[2]
        l_rajonas.append(rajonas)
        l_gatve.append(gatve)

        kaina = elem.find(
            'span', class_='list-item-price').text.strip().replace(' ', '')
        kaina = re.sub(r'\D', '', kaina)
        l_kaina.append(kaina)

        kvadratas = elem.find(
            'span', class_='price-pm').text.strip().replace(' ', '')
        kvadratas = re.sub(r'\D', '', kvadratas)
        l_kvadratas.append(kvadratas)

        kambariai = elem.find('td', class_='list-RoomNum').text.strip()
        l_kambariai.append(kambariai)

        plotas = elem.find(
            'td', class_='list-AreaOverall').text.strip()
        l_plotas.append(plotas)

        aukstai = elem.find(
            'td', class_='list-Floors').text.strip().split('/')
        aukstas = aukstai[0]
        viso_aukstu = aukstai[1]
        l_aukstas.append(aukstas)
        l_aukstu.append(viso_aukstu)
    except Exception:
        None

##########################################
# Visi kiti puslapiai parduodamu butu

i = 2
while i >= 0:
    url = 'https://www.aruodas.lt/butai/vilniuje/puslapis/'+str(i)+'/'
    page = requests.get(url, allow_redirects=False)
    soup = bs(page.content, 'html.parser')

    if page.status_code == 200:
        elems = soup.find_all('tr', class_='list-row')

        for elem in elems:
            try:
                rajonas = elem.find(
                    'td', class_='list-adress').h3.get_text('/').split('/')[1]
                gatve = elem.find(
                    'td', class_='list-adress').h3.get_text('/').split('/')[2]
                l_rajonas.append(rajonas)
                l_gatve.append(gatve)

                kaina = elem.find(
                    'span', class_='list-item-price').text.strip().replace(' ', '')
                kaina = re.sub(r'\D', '', kaina)
                l_kaina.append(kaina)

                kvadratas = elem.find(
                    'span', class_='price-pm').text.strip().replace(' ', '')
                kvadratas = re.sub(r'\D', '', kvadratas)
                l_kvadratas.append(kvadratas)

                kambariai = elem.find('td', class_='list-RoomNum').text.strip()
                l_kambariai.append(kambariai)

                plotas = elem.find(
                    'td', class_='list-AreaOverall').text.strip()
                l_plotas.append(plotas)

                aukstai = elem.find(
                    'td', class_='list-Floors').text.strip().split('/')
                aukstas = aukstai[0]
                viso_aukstu = aukstai[1]
                l_aukstas.append(aukstas)
                l_aukstu.append(viso_aukstu)
            except Exception:
                None
        i += 1
    else:
        break

butai_pardavimui = pd.DataFrame(
    {
        'Rajonas': l_rajonas,
        'Gatve': l_gatve,
        'Kaina': l_kaina,
        'Kvadrato kaina': l_kvadratas,
        'Kambariai': l_kambariai,
        'Plotas': l_plotas,
        'Aukstas': l_aukstas,
        'Is viso aukstu': l_aukstu
    })

### Nuoma

ln_rajonas = []
ln_gatve = []
ln_kaina = []
ln_kvadratas = []
ln_kambariai = []
ln_plotas = []
ln_aukstas = []
ln_aukstu = []

##########################################
# Pirmas Puslapis nuomojamu butu

url = 'https://www.aruodas.lt/butu-nuoma/vilniuje/'
page = requests.get(url, allow_redirects=False)
soup = bs(page.content, 'html.parser')

if page.status_code == 200:
    elems = soup.find_all('tr', class_='list-row')

    for elem in elems:
        try:
            rajonas = elem.find(
                'td', class_='list-adress').h3.get_text('/').split('/')[1]
            gatve = elem.find(
                'td', class_='list-adress').h3.get_text('/').split('/')[2]
            ln_rajonas.append(rajonas)
            ln_gatve.append(gatve)

            kaina = elem.find(
                'span', class_='list-item-price').text.strip().replace(' ', '')
            kaina = re.sub(r'\D', '', kaina)
            ln_kaina.append(kaina)

            kvadratas = elem.find(
                'span', class_='price-pm').text.replace('€/m²', '').strip()
            ln_kvadratas.append(kvadratas)

            kambariai = elem.find('td', class_='list-RoomNum').text.strip()
            ln_kambariai.append(kambariai)

            plotas = elem.find(
                'td', class_='list-AreaOverall').text.strip()
            ln_plotas.append(plotas)

            aukstai = elem.find(
                'td', class_='list-Floors').text.strip().split('/')
            aukstas = aukstai[0]
            viso_aukstu = aukstai[1]
            ln_aukstas.append(aukstas)
            ln_aukstu.append(viso_aukstu)
        except Exception:
            None

##########################################
# Visi kiti puslapiai nuomojami butai

i = 2
while i > 0:
    url = 'https://www.aruodas.lt/butu-nuoma/vilniuje/puslapis/' + str(i)+'/'
    page = requests.get(url, allow_redirects=False)
    soup = bs(page.content, 'html.parser')

    if page.status_code == 200:
        elems = soup.find_all('tr', class_='list-row')

        for elem in elems:
            try:
                rajonas = elem.find(
                    'td', class_='list-adress').h3.get_text('/').split('/')[1]
                gatve = elem.find(
                    'td', class_='list-adress').h3.get_text('/').split('/')[2]
                ln_rajonas.append(rajonas)
                ln_gatve.append(gatve)

                kaina = elem.find(
                    'span', class_='list-item-price').text.strip().replace(' ', '')
                kaina = re.sub(r'\D', '', kaina)
                ln_kaina.append(kaina)

                kvadratas = elem.find(
                    'span', class_='price-pm').text.replace('€/m²', '').strip()
                ln_kvadratas.append(kvadratas)

                kambariai = elem.find('td', class_='list-RoomNum').text.strip()
                ln_kambariai.append(kambariai)

                plotas = elem.find(
                    'td', class_='list-AreaOverall').text.strip()
                ln_plotas.append(plotas)

                aukstai = elem.find(
                    'td', class_='list-Floors').text.strip().split('/')
                aukstas = aukstai[0]
                viso_aukstu = aukstai[1]
                ln_aukstas.append(aukstas)
                ln_aukstu.append(viso_aukstu)
            except Exception:
                None
        i += 1
    else:
        break

butai_nuoma = pd.DataFrame(
    {
        'Rajonas': ln_rajonas,
        'Gatve': ln_gatve,
        'Kaina': ln_kaina,
        'Kvadrato kaina': ln_kvadratas,
        'Kambariai': ln_kambariai,
        'Plotas': ln_plotas,
        'Aukstas': ln_aukstas,
        'Is viso aukstu': ln_aukstu
    })

def csv():
    butai_pardavimui.to_csv('butai_pardavimui.csv')
    butai_nuoma.to_csv('butai_nuoma.csv')

csv()