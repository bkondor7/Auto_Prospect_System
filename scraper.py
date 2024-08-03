import requests
from bs4 import BeautifulSoup

# Scraper
def scrape_listings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    listings = []
    for listing in soup.find_all('div', class_='listing'):
        title = listing.find('h2').text
        price = listing.find('span', class_='price').text
        contact = listing.find('a', class_='contact').get('href')
        
        listings.append({
            'title': title,
            'price': price,
            'contact': contact
        })
    
    return listings