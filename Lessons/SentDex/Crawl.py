import bs4 as bs
import urllib.request

link = 'https://pythonprogramming.net/parsememcparseface/'

# .read() returns src code
sauce = urllib.request.urlopen(link).read()
# Making a BeautifulSoup obj (src_code, parser)
# parsers = ['html.parser', 'xml', 'lxml', 'html5lib', 'lxml-xml']
soup = bs.BeautifulSoup(sauce, 'lxml')

print(soup.find_all('p'))
