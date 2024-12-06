import scrapy

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):

        for book in response.css('article.product_pod'):
            title = book.css('h3 a::attr(title)').get()
            price = book.css('p.price_color::text').get()
            availability = book.css('p.instock.availability::text').get().strip()
            rating = book.css('p.star-rating::attr(class)').re_first(r'star-rating (\w+)')
            book_link = book.css('h3 a::attr(href)').get()
            book_detail_url = response.urljoin(book_link)


            yield response.follow(book_detail_url, self.parse_book_details, meta={
                'title': title,
                'price': price,
                'availability': availability,
                'rating': rating
            })


        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_book_details(self, response):
        genre = response.css('ul.breadcrumb li:nth-child(3) a::text').get().strip()
        

        yield {
            'Title': response.meta['title'],
            'Price': response.meta['price'],
            'Availability': response.meta['availability'],
            'Rating': response.meta['rating'],
            'category': genre
        } 
