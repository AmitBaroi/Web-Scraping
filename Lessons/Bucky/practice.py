import urllib.request
import random


def get_img_from_web(url):
    """Downloads an Image from the web"""
    name = random.randint(1, 1000)
    if name < 10:
        fileName = '000'+str(name) + '.jpg'
    elif name < 100:
        fileName = '00'+str(name) + '.jpg'
    elif name < 1000:
        fileName = '0'+str(name) + '.jpg'

    # Retrieves (downloads) file from given url
    urllib.request.urlretrieve(url, fileName)
    print('DONE!\nSuccessfully downloaded image at project directory!')


link = 'http://srv2.cinehub24.com/images/articles/60427-87325.png'

get_img_from_web(link)
