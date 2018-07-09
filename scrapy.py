from bs4 import BeautifulSoup
from requests import get

url = 'https://ganjoor.net/hafez/ghazal/sh'

# response = get(url)
f = open("sher.txt","a")
for i in range (253,495):
    url2 = url+str(i+1)
    response = get(url2)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    mesra1 = html_soup.find_all('div', class_ = 'm1')
    mesra2 = html_soup.find_all('div', class_ = 'm2')
    print(str(i+1)+"غزل شماره ")
    f.write( str(i+1)+"غزل شماره " )
    f.write("\n")
    i=0
    while i <len(mesra1) :
        f.write(mesra1[i].text+"     "+mesra2[i].text)
        f.write("\n")
        i+=1
f.close()