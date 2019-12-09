from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv;

def getWebpage(url, hdr):
    page = Request(url, headers=hdr)
    page = urlopen(page).read()
    return BeautifulSoup(page, "html.parser")

def write(writer, elems):
        writer.writerow(elems);

def main():
    generesOutput = open('genres.csv', 'w', encoding='utf8')    
    writer =  csv.writer(generesOutput, delimiter=',', lineterminator='\n');

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    genresDict = {'pop-songs' : 'Pop',
                'top-country' : 'Country', 
                'top-rock' : 'Rock', 
                'top-r-and-b-hip-hop' : 'HipHop', 
                'top-christian' : 'Christian', 
                'reggae-albums' : 'Reggae', 
                'blues-albums' : 'Blues', 
                'jazz-albums' : 'Jazz'}
       

    write(writer, ("Genre", "Artists"))

    for genre in genresDict:
        url = "https://www.billboard.com/charts/year-end/"+genre+"-artists"
        soup = getWebpage(url, hdr)

        for artist in soup.findAll("div", attrs={"class": "ye-chart-item__title"}):
            artist = str(artist).split("\n") [-3].rstrip()
            if artist [0] == " ":   
                artist = artist[1:]
            write(writer, (genresDict[genre], artist))

if __name__ == "__main__":
    main()
