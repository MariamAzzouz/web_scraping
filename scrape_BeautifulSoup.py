import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL of the website to scrape
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# List to store book data
books_data = []

# Function to scrape book data from a single page
def scrape_books(page_number):
    response = requests.get(base_url.format(page_number))
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all book containers
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        rating = book.find('p', class_='star-rating')['class'][1]  # Get the rating class

        # Get the link to the book detail page
        book_link = book.h3.a['href']
        book_detail_url = 'https://books.toscrape.com/catalogue/' + book_link

        # Fetch the book detail page to get the genre
        detail_response = requests.get(book_detail_url)
        detail_soup = BeautifulSoup(detail_response.text, 'html.parser')

        # Extract genre from the detail page
        genre = detail_soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip()  # Genre is the third item

        # Append book data to the list
        books_data.append({
            'Title': title,
            'Price': price,
            'Availability': availability,
            'Rating': rating,
            'Genre': genre
        })

# Loop through all pages
for page in range(1, 51):  # Adjust the range as needed (1 to 50 for 50 pages)
    scrape_books(page)

# Create a DataFrame and save to CSV
df = pd.DataFrame(books_data)
df.to_csv('books_data.csv', index=False)

print("Data scraped and saved to books_data.csv")