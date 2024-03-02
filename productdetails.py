import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import json
import sqlite3
from multiprocessing import connection
import time


# ProductDetails Interface 
class BaseProductDetails:
    def __init__(self, brand, model, url, price):
        self.ref_no = ''
        self.brand = brand
        self.model = model
        self.price = price
        self.url = url
        self.image={} # will be converted to json
        self.detail={} # will be converted to json
        db_path = r'D:\office\scraper\scraperapi\db.sqlite3'
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def GetSourceCode(self):
        try:
            r = requests.get(self.url)
            time.sleep(5)
            r.raise_for_status()  # Raise an HTTPError for bad responses
            if r.status_code == 200:
                soup = BeautifulSoup(r.content, 'lxml')
                self.GetDetails(soup)
                print(self.detail)
                self.GetImages(soup)
                print(self.image)
                print("\n\n\n")
                # self.ConvertToJson()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching source code: {e}")

    def ConvertToJson(self):
        images = json.dumps(self.image)
        details = json.dumps(self.detail)
        self.SaveToDatabase(details, images)

    def SaveToDatabase(self, details, images):
        try:
            self.connection.execute('insert into api_product values(?,?,?,?,?,?,?,?)',[self.ref_no,self.brand,self.model,self.price,self.thumbnail,images,self.url,details])
            self.connection.commit()
            print("Saved to database")
        except sqlite3.Error as e:
            print(f"Error saving to database: {e}")

    def GetImages(self, soup):
        # Default implementation
        pass

    def GetDetails(self, soup):
        # Default implementation
        pass

class BuchererProductDetails(BaseProductDetails):
    def GetImages(self, soup):
        try:
            imagesLink=soup.find('div',attrs={"class":"m-product-slider__main js-m-product-slider__main"}).children
            for index, imageLink in enumerate(imagesLink):
                imageTag = imageLink.find('img')
                if imageTag != -1:
                    imageName = imageTag.get('alt')+" #"+str(index+1)
                    image = imageTag.get('data-srcset')
                    self.image[imageName] = image
        except AttributeError as e:
            print(f"Error getting images: {e}")

    def GetDetails(self, soup):
        try:
            details=soup.find_all('div',attrs={"class":"m-product-specification__item"})
            for attr in details:
                name=attr.find('span',attrs={"class":"m-product-specification__label"}).get_text().replace('\n','')
                value=attr.find('span',attrs={"class":"m-product-specification__name"}).get_text().replace('\n','')
                self.detail[name] = value
            self.ref_no=self.detail['Ref.']
        except AttributeError as e:
            print(f"Error getting details: {e}")
        
class ThewatchboxProductDetails(BaseProductDetails):
    def GetImages(self, soup):
        try:
            imagesLink=soup.find_all('img',attrs={"class":"pdp-zoom-load zoomload img-fluid lazyload"})
            for index, imageLink in enumerate(imagesLink):
                imageName = imageLink.get('alt')+" #"+str(index+1)
                image = imageLink.get('data-src')
                self.image[imageName] = image
        except AttributeError as e:
            print(f"Error getting images: {e}")

    def GetDetails(self, soup):
        try:
            description=soup.find('div',attrs={"itemprop":"description"}).get_text().replace('\n','')
            details=soup.find_all('div',attrs={"class":"pdp-refine"})
            for attr in details:
                detail=attr.find_all('span')
                name=detail[0].get_text().replace('\n','').replace(':','')
                value=detail[1].get_text().replace('\n','')
                self.detail[name] = value
            self.detail['Description']=description
            self.ref_no=self.detail['Reference Number']
        except AttributeError as e:
            print(f"Error getting details: {e}")

class TourneauProductDetails(BaseProductDetails):
    def GetImages(self, soup):
        try:
            imagesLink=soup.find('div',attrs={"class":"m-product-slider__main js-m-product-slider__main"}).children
            for imageLink in imagesLink:
                imageTag = imageLink.find('img')
                if imageTag != -1:
                    imageName = imageTag.get('alt')
                    image = imageTag.get('data-srcset')
                    self.image[imageName] = image
        except AttributeError as e:
            print(f"Error getting images: {e}")

    def GetDetails(self, soup):
        try:
            details=soup.find_all('div',attrs={"class":"m-product-specification__item"})
            for attr in details:
                name=attr.find('span',attrs={"class":"m-product-specification__label"}).get_text().replace('\n','')
                value=attr.find('span',attrs={"class":"m-product-specification__name"}).get_text().replace('\n','')
                self.detail[name] = value
            self.ref_no=self.detail['Ref.']
        except AttributeError as e:
            print(f"Error getting details: {e}")

class CrownandcaliberProductDetails(BaseProductDetails):
    def GetImages(self, soup):
        try:
            imagesLink=soup.find('div',attrs={"class":"m-product-slider__main js-m-product-slider__main"}).children
            for imageLink in imagesLink:
                imageTag = imageLink.find('img')
                if imageTag != -1:
                    imageName = imageTag.get('alt')
                    image = imageTag.get('data-srcset')
                    self.image[imageName] = image
        except AttributeError as e:
            print(f"Error getting images: {e}")

    def GetDetails(self, soup):
        try:
            details=soup.find_all('div',attrs={"class":"m-product-specification__item"})
            for attr in details:
                name=attr.find('span',attrs={"class":"m-product-specification__label"}).get_text().replace('\n','')
                value=attr.find('span',attrs={"class":"m-product-specification__name"}).get_text().replace('\n','')
                self.detail[name] = value
            self.ref_no=self.detail['Ref.']
        except AttributeError as e:
            print(f"Error getting details: {e}")

class BobswatchesProductDetails(BaseProductDetails):
    def GetImages(self, soup):
        try:
            imagesLink=soup.find('div',attrs={"class":"m-product-slider__main js-m-product-slider__main"}).children
            for imageLink in imagesLink:
                imageTag = imageLink.find('img')
                if imageTag != -1:
                    imageName = imageTag.get('alt')
                    image = imageTag.get('data-srcset')
                    self.image[imageName] = image
        except AttributeError as e:
            print(f"Error getting images: {e}")

    def GetDetails(self, soup):
        try:
            details=soup.find_all('div',attrs={"class":"m-product-specification__item"})
            for attr in details:
                name=attr.find('span',attrs={"class":"m-product-specification__label"}).get_text().replace('\n','')
                value=attr.find('span',attrs={"class":"m-product-specification__name"}).get_text().replace('\n','')
                self.detail[name] = value
            self.ref_no=self.detail['Ref.']
        except AttributeError as e:
            print(f"Error getting details: {e}")

class GoldsmithsProductDetails(BaseProductDetails):
    def GetImages(self, soup):
        print("\n\n")
        try:
            imagesLink=soup.find_all('div',attrs={"class":"item productImageGallery-Standard"})
            for index, imageLink in enumerate(imagesLink):
                imageTag = imageLink.find('img')
                if imageTag != -1:
                    imageName = imageTag.get('alt')+" #"+str(index+1)
                    image = imageTag.get('src')
                    self.image[imageName] = image
        except AttributeError as e:
            print(f"Error getting images: {e}")

    def GetDetails(self, soup):
        try:
            detailsCon=soup.find('div',attrs={"class":"productPageCollapsibleSectionBody productSpecification"})
            details=detailsCon.find_all('li')
            # details=soup.find_all('ul',attrs={"class":"productSpecs"})[1].find_all('li')
            for attr in details:
                name=attr.find('span',attrs={"class":"specLabel"}).get_text().replace('\n','')
                value=attr.find('span',attrs={"class":"specValue"}).get_text().replace('\n','')
                self.detail[name] = value
            #Description
            descriptionCon=soup.find('div',attrs={"id":"productPageCollapsibleSectionBody"})
            descriptionParagraphs=descriptionCon.find_all('p')
            if len(descriptionParagraphs) >= 1:
                for index, descriptionParagraph in enumerate(descriptionParagraphs):
                    description=descriptionParagraph.get_text().replace('\n','').replace('"','')
                    self.detail['Description #'+str(index+1)]=description
            else:
                description=descriptionCon.get_text().replace('\n','').replace('"','')
                self.detail['Description #1']=description
            self.ref_no=self.detail['Product Code']
        except AttributeError as e:
            print(f"Error getting details: {e}")

class WatchesofswitzerlandProductDetails(BaseProductDetails):
    def GetImages(self, soup):
        print("\n\n")
        try:
            imagesLink=soup.find_all('div',attrs={"class":"item productImageGallery-Standard"})
            for index, imageLink in enumerate(imagesLink):
                imageTag = imageLink.find('img')
                if imageTag != -1:
                    imageName = imageTag.get('alt')+" #"+str(index+1)
                    image = imageTag.get('src')
                    self.image[imageName] = image
        except AttributeError as e:
            print(f"Error getting images: {e}")

    def GetDetails(self, soup):
        try:
            detailsCon=soup.find('div',attrs={"class":"productPageCollapsibleSectionBody productSpecification"})
            details=detailsCon.find_all('li')
            # details=soup.find_all('ul',attrs={"class":"productSpecs"})[1].find_all('li')
            for attr in details:
                name=attr.find('span',attrs={"class":"specLabel"}).get_text().replace('\n','')
                value=attr.find('span',attrs={"class":"specValue"}).get_text().replace('\n','')
                self.detail[name] = value
            #Description
            descriptionCon=soup.find('div',attrs={"id":"productPageCollapsibleSectionBody"})
            descriptionParagraphs=descriptionCon.find_all('p')
            if len(descriptionParagraphs) >= 1:
                for index, descriptionParagraph in enumerate(descriptionParagraphs):
                    description=descriptionParagraph.get_text().replace('\n','').replace('"','')
                    self.detail['Description #'+str(index+1)]=description
            else:
                description=descriptionCon.get_text().replace('\n','').replace('"','')
                self.detail['Description #1']=description
            self.ref_no=self.detail['Product Code']
        except AttributeError as e:
            print(f"Error getting details: {e}")

class Chrono24ProductDetails(BaseProductDetails):
    def GetSourceCode(self):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                try:
                    page.goto(self.url)
                    # Wait for network idle
                    page.wait_for_load_state("networkidle")
                    # Get the HTML after JavaScript execution
                    soup = BeautifulSoup(page.content(), 'lxml')
                    self.GetDetails(soup)
                    print(self.detail)
                    self.GetImages(soup)
                    print(self.image)
                    print("\n\n\n")
                    # self.ConvertToJson()
                finally:
                    # Ensure the browser is closed even if an error occurs
                    browser.close()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching source code: {e}")
    def GetImages(self, soup):
        try:
            imagesCon=soup.find_all('div',attrs={"class":"js-carousel-zoom-image-container"})
            for index,imageLink in enumerate(imagesCon):
                imageName = 'image #'+str(index+1)
                image = imageLink.get('data-zoom-image')
                self.image[imageName] = image
        except AttributeError as e:
            print(f"Error getting images: {e}")

    def GetDetails(self, soup):
        try:
            detailsCon=soup.find_all('div',attrs={"class":"col-xs-24 col-md-12"})[0]
            details=detailsCon.find_all('tr')
            for attr in details:
                if attr.find('td', {'colspan': '2'}):
                    continue
                _detail=attr.find_all('td')
                name=_detail[0].get_text(strip=True).replace('\n','')
                value=_detail[1].get_text().replace('\n','')
                self.detail[name] = value
            self.ref_no=self.detail['Reference number']
            self.model = self.detail['Model'] if 'Model' in self.detail else self.detail['Reference number']
            self.brand=self.detail['Brand']
            descriptionCon=soup.find('span',attrs={"id":"watchNotes"})
            if descriptionCon:
                description=descriptionCon.get_text(strip=True)
                self.detail['Description']=description
        except AttributeError as e:
            print(f"Error getting details: {e}")

class JomashopProductDetails(BaseProductDetails):
    def GetSourceCode(self):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                try:
                    page.goto(self.url)
                    # Wait for network idle
                    page.wait_for_load_state("networkidle")
                    # Get the HTML after JavaScript execution
                    soup = BeautifulSoup(page.content(), 'lxml')
                    self.GetDetails(soup)
                    print(self.detail)
                    self.GetImages(soup)
                    print(self.image)
                    print("\n\n\n")
                    # self.ConvertToJson()
                finally:
                    # Ensure the browser is closed even if an error occurs
                    browser.close()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching source code: {e}")
    def GetImages(self, soup):
        try:
            imagesLink=soup.find_all('img',attrs={"class":"slide-item-main-image"})
            for index,imageLink in enumerate(imagesLink):
                imageName = imageLink.get('title')+" #"+str(index+1)
                image = imageLink.get('src')
                self.image[imageName] = image
        except AttributeError as e:
            print(f"Error getting images: {e}")

    def GetDetails(self, soup):
        try:
            description=soup.find('div',attrs={"class":"desc-content"}).get_text().replace('\n','')
            details=soup.find_all('div',attrs={"class":"more-detail-content"})
            for attr in details:
                name=attr.find('h4',attrs={"class":"more-label"}).get_text(strip=True).replace('\n','')
                value=attr.find('span',attrs={"class":"more-value"}).get_text().replace('\n','')
                self.detail[name] = value
            self.ref_no=self.detail['Model']
            self.detail['Description']=description
        except AttributeError as e:
            print(f"Error getting details: {e}")

class MayorsProductDetails(BaseProductDetails):
    def GetImages(self, soup):
        print("\n\n")
        try:
            imagesLink=soup.find_all('div',attrs={"class":"item productImageGallery-Standard"})
            for index, imageLink in enumerate(imagesLink):
                imageTag = imageLink.find('img')
                if imageTag != -1:
                    imageName = imageTag.get('alt')+" #"+str(index+1)
                    image = imageTag.get('src')
                    self.image[imageName] = image
        except AttributeError as e:
            print(f"Error getting images: {e}")

    def GetDetails(self, soup):
        try:
            details=soup.find_all('ul',attrs={"class":"productSpecs"})[1].find_all('li')
            for attr in details:
                name=attr.find('span',attrs={"class":"specLabel"}).get_text().replace('\n','')
                value=attr.find('span',attrs={"class":"specValue"}).get_text().replace('\n','')
                self.detail[name] = value
            #Description
            descriptionCon=soup.find('div',attrs={"id":"productPageCollapsibleSectionBody"})
            descriptionParagraphs=descriptionCon.find_all('p')
            if len(descriptionParagraphs) >= 1:
                for index, descriptionParagraph in enumerate(descriptionParagraphs):
                    description=descriptionParagraph.get_text().replace('\n','').replace('"','')
                    self.detail['Description #'+str(index+1)]=description
            else:
                description=descriptionCon.get_text().replace('\n','').replace('"','')
                self.detail['Description #1']=description
            self.ref_no=self.detail['Product Code']
        except AttributeError as e:
            print(f"Error getting details: {e}")

class BeyerchProductDetails(BaseProductDetails):
    def GetImages(self, soup):
        try:
            imagesCon=soup.find_all('a',class_=['imglink','imglink--lightbox'])
            for index,imageCon in enumerate(imagesCon):
                    imageLink=imageCon.find('img')
                    imageName = imageLink.get('alt')+" #"+str(index+1)
                    image = imageLink.get('data-srcset')
                    self.image[imageName] = image
        except AttributeError as e:
            print(f"Error getting images: {e}")

    def GetDetails(self, soup):
        try:
            details=soup.find('table',attrs={"class":"productnew-detail__table"}).children
            for attr in details:
                _detail=attr.find_all('td')
                name=_detail[0].get_text().replace('\n','')
                value=_detail[1].get_text().replace('\n','')
                self.detail[name] = value
            self.ref_no=self.detail['Ref.']
        except AttributeError as e:
            print(f"Error getting details: {e}")