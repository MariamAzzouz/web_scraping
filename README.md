# Web Scraping Project

## Overview

This repository contains two implementations of a web scraping project aimed at extracting book data from the website [Books to Scrape](https://books.toscrape.com). The project serves as a personal enhancement exercise to practice the basics of web scraping using two different libraries: **BeautifulSoup** and **Scrapy**. 

## Purpose

The main goal of this project is to gain hands-on experience with web scraping techniques, understand the differences between using BeautifulSoup and Scrapy, and improve my skills in data extraction and manipulation.

## Project Structure

The repository consists of the following files:

- `scrape_BeautifulSoup.py`: A Python script that uses the BeautifulSoup library to scrape book data from the website.
- `books_scraper/books_scraper/spiders/books_spider.py`: A Scrapy spider that performs the same scraping task using the Scrapy framework.

## Libraries Used

- **BeautifulSoup**: A Python library for parsing HTML and XML documents. It creates parse trees from page source codes that can be used to extract data easily.
- **Scrapy**: An open-source and collaborative web crawling framework for Python. It is used to extract the data from the website and store it in a structured format.

## How to Run the Project

### Using BeautifulSoup

1. Ensure you have Python installed on your machine.
2. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```
3. Run the BeautifulSoup script:
   ```bash
   python scrape_BeautifulSoup.py
   ```

### Using Scrapy

1. Ensure you have Python and Scrapy installed on your machine.
2. Navigate to the Scrapy project directory:
   ```bash
   cd books_scraper
   ```
3. Install the required libraries:
   ```bash
   pip install scrapy
   ```
4. Run the Scrapy spider:
   ```bash
   scrapy crawl books -o books_data.csv
   ```

## Output

Both implementations will scrape book data, including the title, price, availability, rating, and category, and save the data to a CSV file named `books_data.csv`.

## Conclusion

This project has provided valuable insights into web scraping techniques and the differences between using BeautifulSoup and Scrapy. It has enhanced my understanding of data extraction and manipulation, which are essential skills in data science and web development.
