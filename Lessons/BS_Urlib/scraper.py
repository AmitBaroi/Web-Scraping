from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup

# The web-page (single page html) we will work with
url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards"

# Requesting the site for the page
uClient = uReq(url)
# Storing response html in var
page_html = uClient.read()
# Closing connection
uClient.close()
# Parsing html for easy access
page_soup = Soup(page_html, "html.parser")

# Isolating the divs that hold each products info
containers = page_soup.findAll("div", {"class": "item-container"})

# Setting up file for saving data
fName = "product_data.csv"
file = open(fName, "w")
headers = "Brand, Product_name, Shipping\n"
file.write(headers)

# Grabs relevant info from each product
for container in containers:
    # Gets the brand name
    brand = container.div.div.a.img["title"].replace(",", "|")

    # Gets the product name
    title_container = container.findAll("a", {"class": "item-title"})
    prod_name = title_container[0].text.replace(",", "|")

    # Gets shipping info for the product
    ship_cont = container.findAll("li", {"class": "price-ship"})
    shipping = ship_cont[0].text.strip().replace(",", "|")

    print("Brand", brand)
    print("Product", prod_name)
    print("Shipping", shipping)

    file.write(brand + "," + prod_name + "," + shipping + "\n")
