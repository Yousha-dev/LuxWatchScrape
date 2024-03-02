import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options

# ProductsPage Interface 
class BaseProductsPage:
    def __init__(self,url):
        self.url = url
        self.productPages = []

    def GetSourceCode(self):
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without a visible window)
        with webdriver.Chrome(options=webdriver.ChromeOptions()) as driver:
            driver.get(self.url)
            time.sleep(3)
            self.ScrollDown(driver)
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            self.GetProductsInfo(soup)
        return self.productPages
    
    def ScrollDown(self, driver):
        scroll_pause_time = 0.4  # You can set your own pause time. 
        screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
        i = 0.4
        while True:
            # scroll one screen height each time
            driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
            i += 0.4
            time.sleep(scroll_pause_time)
            # check the page scroll position
            scroll_height = driver.execute_script("return document.body.scrollHeight;")  
            # break the loop when the height we need to scroll to is larger than the total scroll height
            if (screen_height) * i > scroll_height:
                break 

    def GetProductsInfo(self, soup):
        # Default implementation
        pass

class BuchererProductsPage(BaseProductsPage):
    def GetProductsInfo(self, soup):
        products = soup.find_all('a', attrs={"class": "m-product-tile__link"})
        for product in products:
            link = "https://www.bucherer.com/" + product.get('href')
            brand = product.find('span', attrs={"class": "m-product-tile__product-brand"}).get_text().replace("\n", "")
            model = product.find('span', attrs={"class": "m-product-tile__product-model"}).get_text().replace("\n", "")
            price = product.find('span', attrs={"class": "value"}).get_text().replace(" ", "").replace("\n", "").replace("'", "").replace(",", "")
            self.productPages.append((brand, model, link, price))

class ThewatchboxProductsPage(BaseProductsPage):
    def GetProductsInfo(self, soup):
        products = soup.find_all('a', attrs={"class": "link grid-carousel-link"})
        for product in products:
            link = "https://www.thewatchbox.com" + product.get('href')
            brand = product.find('div', attrs={"class": "grid__brand"}).get_text().replace("\n", "")
            model = product.find('span', attrs={"class": "grid__name"}).get_text().replace("\n", "")
            priceCon = product.find('div', attrs={"class": "grid__price"})
            price=priceCon.find('span').get_text().replace(" ", "").replace("\n", "").replace("'", "").replace(",", "")
            self.productPages.append((brand, model, link, price))

class TourneauProductsPage(BaseProductsPage):
    def GetProductsInfo(self, soup):
        products = soup.find_all('li', attrs={"class": "grid-tile"})
        for product in products:
            link = product.find('a', attrs={"class": "thumb-link"}).get('href')
            brand = product.find('div', attrs={"class": "brand"}).get_text().replace("\n", "")
            model = product.find('a', attrs={"class": "name-link"}).get_text().replace("\n", "")
            price = product.find('span', attrs={"class": "product-sales-price"}).get_text().replace(" ", "").replace("\n", "").replace("'", "").replace(",", "")
            self.productPages.append((brand, model, link, price))

class CrownandcaliberProductsPage(BaseProductsPage):
    def GetProductsInfo(self, soup):
        products = soup.find_all('div', attrs={"class": "cell small-12 medium-4 ss-item ng-scope"})
        print(products)
        for product in products:
            productCon = product.find('a', attrs={"class": "grid-view-item__link"})
            link = productCon.get('href')
            brand = productCon.find('div', attrs={"class": "card-title ng-binding"}).get_text().replace("\n", "")
            model = productCon.find('div', attrs={"class": "card-subTitle ng-binding"}).get_text().replace("\n", "")
            price = productCon.find('span', attrs={"class": "current-price product-price__price ng-binding"}).get_text().replace(" ", "").replace("\n", "").replace("'", "").replace(",", "")
            self.productPages.append((brand, model, link, price))

class BobswatchesProductsPage(BaseProductsPage):
    def GetProductsInfo(self, soup):
        products = soup.find_all('div', attrs={"class": "itemWrapper ng-scope"})
        # print(products)
        for product in products:
            productCon = product.find('a', attrs={"itemprop": "url"})
            link = self.url + productCon.get('href')
            brand = productCon.find('meta', attrs={"itemprop": "brand"}).get('content').replace("\n", "")
            modelCon = productCon.find('span', attrs={"itemprop": "name"})
            model=modelCon.find('span').get_text().replace("\n", "").replace(brand, "").replace("\n", "").replace("\t", "").replace("  ", "")
            priceCurrency = productCon.find('span', attrs={"itemprop": "priceCurrency"}).get_text()
            price = priceCurrency+productCon.find('span', attrs={"itemprop": "price"}).get_text()
            price=price.replace(" ", "").replace("\n", "").replace("'", "").replace(",", "")
            self.productPages.append((brand, model, link, price))

class GoldsmithsProductsPage(BaseProductsPage):
    def GetProductsInfo(self, soup):
        products = soup.find_all('div', attrs={"class": "productTile"})
        for product in products:
            productCon = product.find('a')
            link = "https://www.goldsmiths.co.uk" + productCon.get('href')
            brand = productCon.find('div', attrs={"class": "productTileBrand"}).get_text().replace("\n", "")
            model_full = productCon.find('div', attrs={"class": "productTileName"}).get_text().replace("\n", "")
            model = model_full.split("mm")[0].rsplit(' ', 1)[0]
            price = productCon.find('div', attrs={"class": "productTilePrice"}).get_text().replace("\n", "").replace("\t", "").replace(",", "").replace(" ", "")
            price = re.sub(r'(\d+\.00)(£)', r'\1 \2', price)
            self.productPages.append((brand, model, link, price))

class WatchesofswitzerlandProductsPage(BaseProductsPage):
    def GetProductsInfo(self, soup):
        products = soup.find_all('div', attrs={"class": "productTile"})
        for product in products:
            productCon = product.find('a')
            link = "https://www.watchesofswitzerland.com" + productCon.get('href')
            brand = productCon.find('div', attrs={"class": "productTileBrand"}).get_text().replace("\n", "")
            model_full = productCon.find('div', attrs={"class": "productTileName"}).get_text().replace("\n", "")
            model = model_full.split("mm")[0].rsplit(' ', 1)[0]
            price = productCon.find('div', attrs={"class": "productTilePrice"}).get_text().replace("\n", "").replace("\t", "").replace(",", "").replace(" ", "")
            price = re.sub(r'(\d+\.00)(£)', r'\1 \2', price)
            self.productPages.append((brand, model, link, price))

class Chrono24ProductsPage(BaseProductsPage):
    def GetProductsInfo(self, soup):
        productsCon = soup.find('div', attrs={"class": "js-article-item-list article-item-list article-list block"})
        products = soup.find_all('div', attrs={"class": "article-item-container wt-search-result article-image-carousel"})
        for product in products:
            productCon = product.find('a', attrs={"class": "js-article-item article-item block-item rcard"})
            link = "https://www.chrono24.com" + productCon.get('href')
            brand = ""
            model = ""
            priceCon = productCon.find_all('div', attrs={"class": "text-bold"})[1]
            price = priceCon.get_text().strip().replace("\n", "").replace(" ", "").replace("'", "").replace(",", "")
            priceShipping = productCon.find('div', attrs={"class": "text-muted text-sm"}).get_text().replace("\n", "")
            priceT=price+" "+priceShipping
            self.productPages.append((brand, model, link, priceT))

class JomashopProductsPage(BaseProductsPage):
    def GetProductsInfo(self, soup):
        products = soup.find_all('div', attrs={"class": "productItemBlock"})
        # print(products)
        for product in products:
            link = "https://www.jomashop.com" + product.get('data-scroll-target')
            brand = product.find('span',attrs={"class": "brand-name"}).get_text().replace("\n", "")
            model = product.find('span', attrs={"class": "name-out-brand"}).get_text().replace("\n", "")
            priceCon = product.find('div', attrs={"class": "now-price"})
            priceSpans = priceCon.find_all('span')
            if len(priceSpans) > 1:
                price = priceSpans[1].get_text()
            else:
                price = priceSpans[0].get_text()
            price=price.replace(" ", "").replace("\n", "").replace("'", "").replace(",", "")
            wpriceCon = product.find('div', attrs={"class": "was-wrapper"})
            if wpriceCon:
                wpriceSpans = wpriceCon.find_all('span')
                wprice = wpriceSpans[1].get_text().replace(" ", "").replace("\n", "").replace("'", "").replace(",", "")
                price = price + " " + wprice
            self.productPages.append((brand, model, link, price))

class MayorsProductsPage(BaseProductsPage):
    def GetProductsInfo(self, soup):
        products = soup.find_all('div', attrs={"class": "productTile"})
        for product in products:
            productCon = product.find('a')
            link = "https://www.mayors.com" + productCon.get('href')
            brand = productCon.find('div', attrs={"class": "productTileBrand"}).get_text().replace("\n", "").replace("Pre-Owned ","")
            model_full = productCon.find('div', attrs={"class": "productTileName"}).get_text().replace("\n", "")
            model = model_full.split("mm")[0].rsplit(' ', 1)[0]
            price = productCon.find('div', attrs={"class": "productTilePrice"}).get_text().replace("\n", "").replace("\t", "").replace(",", "").replace(" ", "")
            price = re.sub(r'(\d+\.00)(£)', r'\1 \2', price)
            self.productPages.append((brand, model, link, price))

class BeyerchProductsPage(BaseProductsPage):
    def GetProductsInfo(self, soup):
        products = soup.find_all('a', attrs={"class": "productnew"})
        for product in products:
            link = "https://www.beyer-ch.com" + product.get('href')
            brand = product.find('div', attrs={"class": "productnew__brand"}).get_text().replace("\n", "")
            model = product.find('div', attrs={"class": "productnew__name"}).get_text().replace("\n", "")
            price=product.find('div', attrs={"class": "productnew__price"}).get_text().replace(" ", "").replace("\n", "").replace("'", "").replace(",", "")
            self.productPages.append((brand, model, link, price))

