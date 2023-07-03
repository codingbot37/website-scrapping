import requests
from bs4 import BeautifulSoup
import pandas as pd
from django.http import HttpResponse

def BooksScrapper(request):
    books = []
    for i in range(1, 5):
        url = f"https://books.toscrape.com/catalogue/page-{i}.html"
        response = requests.get(url)
        response = response.content
        soup = BeautifulSoup(response, 'html.parser')
        ol = soup.find('ol')
        articles = ol.find_all('article', class_='product_pod')

        for article in articles:
            image = article.find('img')['src']
            title = article.find('h3').text
            star = article.find('p')
            star = star['class'][1]
            price = article.find('p', class_='price_color').text
            price = float(price[1:])
            books.append([title, price, star , image])

    df = pd.DataFrame(books, columns=['Title', 'Price', 'Star Rating', 'Image'])
    csv_data = df.to_csv(index=False)
    
    # Set the appropriate response headers
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    # Write the CSV data to the response
    response.write(csv_data)

    # Return the response
    return response
