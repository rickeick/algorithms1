# Site está acessível?
import urllib.request

site = 'http://www.pudim.com.br'
try:
    req = urllib.request.urlopen(site)
except:
    print(f'O site {site} NÃO está acessível')
else:
    print(f'O site {site} está acessivel')
