# LuxWatchScrape: Comprehensive Data Extraction for the Luxury Watch Market

Welcome to **LuxWatchScrape**, a powerful, versatile, and efficient web scraper that dives into the world of luxury watches. This Python-based project is designed to extract detailed information about luxury watches from a multitude of online retailers, including but not limited to Chrono24, The Watch Box, Tourneau, Crown & Caliber, Bob's Watches, Goldsmiths, Watches of Switzerland, Jomashop, Mayors, and Beyer.

## Features

- **Multi-Source Data Collection:** LuxWatchScrape is not limited to a single source. It navigates through each website, collecting data such as brand, model, price, and other relevant details.

- **Structured Data Output:** The collected data is organized in a structured format, ready for further analysis or storage.

- **Database Integration:** LuxWatchScrape saves the scraped data to a database, allowing for easy access and management of the collected information.

- **API Access:** The scraped data can be accessed through an API built on the Django REST framework, enabling integration with other applications or services.

- **Extendable Design:** Each retailer has its own class for handling the specific details and structure of that website, making the scraper easily extendable to new sources.

## Technology Stack

LuxWatchScrape is built with Python, utilizing libraries such as BeautifulSoup for HTML parsing and requests for handling HTTP requests. It demonstrates the use of object-oriented programming (OOP) principles to create modular and maintainable code.

## Who is it for?

LuxWatchScrape is ideal for watch enthusiasts, collectors, or businesses looking to gather data for market research, price comparison, or trend analysis across multiple platforms. Dive into the world of luxury watches with LuxWatchScrape!

## Usage

```python
from productspage import BuchererProductsPage
from productdetails import BuchererProductDetails

url="https://www.bucherer.com/buy-watches?"
source = url.split('.')[1]
if source == "bucherer":
    products = BuchererProductsPage(url).GetSourceCode()
else:
    raise Exception('Invalid source')

for brand, model, url, price in products:
    print(f"Source: {source}, Brand: {brand}, Model: {model}, URL: {url}, Price: {price}\n")
    if source == "bucherer":
        product_detail_instance = BuchererProductDetails(brand, model, url, price)
    else:
        raise Exception('Invalid source')
    product_detail_instance.GetSourceCode()
```

The `url` variable should be set to the URL of the website you want to scrape. The `source` variable is determined by splitting the URL at the periods and taking the second element. This is the domain name of the website, which is used to determine which class to use for scraping the website.

Each website has its own class for both the product page and the product details. These classes are used to handle the specific details and structure of each website. The `GetSourceCode()` method is called on the appropriate class to start the scraping process.

After running the scraper, the data is saved to a database. You can access this data through an API built on the Django REST framework. Please refer to the API documentation for more details on how to retrieve the data.

