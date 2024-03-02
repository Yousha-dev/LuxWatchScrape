from productspage import BuchererProductsPage, ThewatchboxProductsPage, TourneauProductsPage, CrownandcaliberProductsPage, BobswatchesProductsPage, GoldsmithsProductsPage, WatchesofswitzerlandProductsPage, Chrono24ProductsPage, JomashopProductsPage, MayorsProductsPage, BeyerchProductsPage
from productdetails import BuchererProductDetails, ThewatchboxProductDetails, TourneauProductDetails, CrownandcaliberProductDetails, BobswatchesProductDetails, GoldsmithsProductDetails, WatchesofswitzerlandProductDetails, Chrono24ProductDetails, JomashopProductDetails, MayorsProductDetails, BeyerchProductDetails

# PRE-OWNED LIST NOT MAINTAINED YET
# https://www.bucherer.com/buy-watches?srule=Global+sorting+rule&start=0&sz=48   
# https://www.thewatchbox.com/watches/shop/all-watches/   
# https://www.tourneau.com/watches/brands/tudor/          
# https://www.crownandcaliber.com/collections/shop-for-watches   
# https://www.bobswatches.com/luxury-watches/    
# https://www.goldsmiths.co.uk/c/Watches?q=&sort=  
# https://www.watchesofswitzerland.com/c/Watches/Mens-Watches
# https://www.chrono24.com/search/index.htm?currencyId=EUR&dosearch=true&gender=1401&maxAgeInDays=0&pageSize=60&redirectToSearchIndex=true&resultview=block&sortorder=0  Brand and model need to be extracted from the url
# https://www.jomashop.com/watches.html
# https://www.mayors.com/c/Watches
# https://www.beyer-ch.com/en/watches/pre-loved-watches/our-range/

url="https://www.thewatchbox.com/watches/shop/all-watches/"
source = url.split('.')[1]
if source == "bucherer":
    products = BuchererProductsPage(url).GetSourceCode()
elif source == "thewatchbox":
    products = ThewatchboxProductsPage(url).GetSourceCode()
elif source == "tourneau":
    products = TourneauProductsPage(url).GetSourceCode()
elif source == "crownandcaliber":
    products = CrownandcaliberProductsPage(url).GetSourceCode()
elif source == "bobswatches":
    products = BobswatchesProductsPage(url).GetSourceCode()
elif source == "goldsmiths":
    products = GoldsmithsProductsPage(url).GetSourceCode()
elif source == "watchesofswitzerland":
    products = WatchesofswitzerlandProductsPage(url).GetSourceCode()
elif source == "chrono24":
    products = Chrono24ProductsPage(url).GetSourceCode()
elif source == "jomashop":
    products = JomashopProductsPage(url).GetSourceCode()
elif source == "mayors":
    products = MayorsProductsPage(url).GetSourceCode()
elif source == "beyer-ch":
    products = BeyerchProductsPage(url).GetSourceCode()
else:
    raise Exception('Invalid source')

for brand, model, url, price in products:
    print(f"Source: {source}, Brand: {brand}, Model: {model}, URL: {url}, Price: {price}\n")
    if source == "bucherer":
        product_detail_instance = BuchererProductDetails(brand, model, url, price)
    elif source == "thewatchbox":
        product_detail_instance = ThewatchboxProductDetails(brand, model, url, price)
    elif source == "tourneau":
        product_detail_instance = TourneauProductDetails(brand, model, url, price)
    elif source == "crownandcaliber":
        product_detail_instance = CrownandcaliberProductDetails(brand, model, url, price)
    elif source == "bobswatches":
        product_detail_instance = BobswatchesProductDetails(brand, model, url, price)
    elif source == "goldsmiths":
        product_detail_instance = GoldsmithsProductDetails(brand, model, url, price)
    elif source == "watchesofswitzerland":
        product_detail_instance = WatchesofswitzerlandProductDetails(brand, model, url, price)
    elif source == "chrono24":
        product_detail_instance = Chrono24ProductDetails(brand, model, url, price)
    elif source == "jomashop":
        product_detail_instance = JomashopProductDetails(brand, model, url, price)
    elif source == "mayors":
        product_detail_instance = MayorsProductDetails(brand, model, url, price)
    elif source == "beyer-ch":
        product_detail_instance = BeyerchProductDetails(brand, model, url, price)
    else:
        raise Exception('Invalid source')
    product_detail_instance.GetSourceCode()