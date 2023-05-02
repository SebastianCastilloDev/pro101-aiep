# Python - Ejercicio 159: Obtener las Últimas Noticias desde Google News con Beautiful Soup 4

from bs4 import BeautifulSoup as soup

from urllib.request import urlopen

url = 'https://news.google.com/news/rss'

cliente = urlopen(url)
contenido_xml = cliente.read()
cliente.close()

# lectura xml

pagina = soup(contenido_xml, 'html.parser')
items = pagina.findAll('item')

for item in items:
    print(item.title.text)
    print(item.link.text)
    # print(item.pub-date.text)

    print('='*40)
