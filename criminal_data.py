''' example from: https://journalistsresource.org/tip-sheets/research/python-scrape-website-data-criminal-justice '''
import requests
from bs4 import BeautifulSoup
from collections import namedtuple

def download_data(how_many):
    ''' downloads data and creates a dictionaty of inmates'''
    url_to_scrape = 'http://apps2.polkcountyiowa.gov/inmatesontheweb/'
    # load the inmates listing
    r = requests.get(url_to_scrape)
    # soup contains the page source
    soup = BeautifulSoup(r.text, "lxml")
    links = []
    # loop over inmates
    for table_row in soup.select(".inmatesList tr")[:how_many + 1]:
        table_cells = table_row.findAll('td')
        if len(table_cells) > 0:
            relative_url = table_cells[0].find('a')['href']
            inmate_url = url_to_scrape + relative_url
            links.append(inmate_url)

    inmates = dict()
    inmate_details = namedtuple('inmate_details',['book_date', 'age', 'race', 'sex', 'city', 'charges'])
    # loop over urls with inmates'details
    for link in links:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'lxml')
        table_rows = soup.select('#inmateNameDate tr')
        name = table_rows[1].findAll('td')[0].text.strip()
        date = table_rows[2].findAll('td')[0].text.strip()

        table_rows = soup.select('#inmateProfile tr')
        age  = table_rows[0].findAll('td')[0].text.strip()
        race = table_rows[3].findAll('td')[0].text.strip()
        sex  = table_rows[4].findAll('td')[0].text.strip()

        city = soup.select('#inmateAddress')[0].text.split('\n')[2].strip()
        table_rows = soup.select('.inmateCharges tr')
        charges = [table_rows[i].findAll('td')[1].text.strip() for i in range(1, len(table_rows))]
        inmates[name] = inmate_details(date, age, race, sex, city, charges)

    # for inmate, details in inmates.items():
    #     print inmate
    #     print charges
    #     print '----'
    return inmates

if __name__ == '__main__':
    download_data()
