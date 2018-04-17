from bs4 import BeautifulSoup
info = []

with open("./class1/index.html","r") as html:
    soup = BeautifulSoup(html,"lxml")
    images = soup.select("body > div > div > div.col-md-9 > div > div > div > img")
    names = soup.select("body > div > div > div.col-md-9 > div > div > div > div > h4 > a")
    prices = soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right")
    views = soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right")
    stars = soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)")
    print(stars)
    for image,name,price,view,star in zip(images,names,prices,views,stars):
        data = {
            "image" : image.get('src'),
            "name" : name.get_text(),
            "price" : price.get_text(),
            "view" : view.get_text(),
            "star" : len(star.find_all("span",class_="glyphicon glyphicon-star"))


        }
        print(data)


