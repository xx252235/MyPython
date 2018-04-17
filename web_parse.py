from bs4 import BeautifulSoup

info = []

with open("D://BaiduNetdiskDownload/web/new_index.html","r") as html:
    soup = BeautifulSoup(html,"lxml")
    images = soup.select("body > div.main-content > ul > li > img")
    titles = soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    cates = soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')
    rates = soup.select('body > div.main-content > ul > li > div.rate > span')

    for title,cate,image,rate in zip(titles,cates,images,rates):
        data = {
            "title":title.get_text(),
            "cate":list(cate.stripped_strings),
            "image":image.get('src'),
            "rate":rate.get_text()

        }
        info.append(data)
    for i in info:
        if float(i["rate"])>3:
            print(i["title"],i["rate"])