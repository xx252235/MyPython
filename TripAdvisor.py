from bs4 import BeautifulSoup
import requests

url = "https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html"

def dataabstraction(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,"lxml")
    titles = soup.select("#ATTR_ENTRY_ > div > div > div > div.listing_info > div.listing_title > a")
    comments = soup.select("#ATTR_ENTRY_ > div > div > div > div > div.listing_rating > div > div > span.more > a")
    ranks = soup.select("#ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.listing_info > div.listing_rating > div:nth-of-type(3)")
    rates = soup.select("#ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.listing_info > div.listing_rating > div:nth-of-type(2) > div > span.ui_bubble_rating.bubble_50")
    # images = soup.select('img[width="180"]')
    for title,comment,rank,rate in zip(titles,comments,ranks,rates):
        data = {
            "title" : title.get_text(),
            "comment" : comment.get_text().replace("\n",""),
            "rank" : rank.get_text().replace("\n",""),
            "rate" : list(rate.find_all("span",class_="ui_bubble_rating bubble_50"))
            # "image" : image.get("src")
        }
        print(data)

dataabstraction(url)

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#     "Cookies":"TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TART=%1%enc%3AVt7%2BLzU0uDV3VCgw5oEzJfaJwtEgV09sWhGEFpn0Dq1E%2B4hvhzCqSYea5QyC%2BvhEDDVmrowwGzE%3D; TAUnique=%1%enc%3A9qBPh2hdE%2BAlPEFsgPfWEhodK3%2BHLp9aHDJDjiyq608BS27FZ6YVQQ%3D%3D; TASSK=enc%3AAG6d4VIs0jzx01KPIAAZvTPLM535rudxQ%2Fdq9%2BYWRskekRj2Bz8H7oL6BIunIOFMdhhdzKUmK%2FrCU6N3PqpzG2SEiFyq42AQ2a64dvex0GYlb7xrONLDIorrwousI%2Ft18Q%3D%3D; _ym_uid=1523524506899467157; _smt_uid=5acf23b3.1c2be709; __gads=ID=72ae81c6235061c1:T=1523524568:S=ALNI_MYLsOm3Gm1V68kAT2CYczODVXK1vQ; _ga=GA1.2.440160704.1523524614; _gid=GA1.2.246553447.1523524614; _ym_hostIndex=0-1%2C1-0; ServerPool=X; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CSPHRSess%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C3%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CSPHRPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7C; VRMCID=%1%V1*id.16631*llp.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*e.1524186828488; ki_r=; CommercePopunder=SuppressAll*1523582069699; SecureLogin2=3.4%3AAIKKAv1hhVIX0PVzgLRFN%2BdIYQPXc%2Bjp3ehyiDHh47X66XAZBs9f91zCJr%2FZMJf8n48dx7dnVz7sy%2FSrKNc%2FlhZd5Smg%2FD23lICPIqW8v505FwlFGXR6xOFaz%2BiBuyUac6L5V18%2FEbVtDYhZqwbEet4%2BoJIgP7DvRhVuO99qJxdOUMD5yB5Iz2X9lF48n46gIANkhCeSsYGQtZ0By3U%2F8pc%3D; TAAuth3=3%3A82ffaee06eac93dc302dc8081b94e409%3AAEh%2F4ShYYmK%2Fc6RYxOWLSh54XhqMXvKW4KACpkdP3lu2Ik42H56mbx8rQ1XalGYrk8vnjGbvSqpJ6oqBj34ijulW87wqHHvIFZN10H3MfPGsBbyhBz6VcCkdFpmPDIOzgl2z8hRQan7fHjBYQG3KbLjojN%2BSsklvHd%2BMWoF4zghXahP0WOix9mpZ%2FCqKUVeJ0g%3D%3D; TAReturnTo=%1%%2FAttraction_Review-g60763-d267031-Reviews-Manhattan_Skyline-New_York_City_New_York.html; ki_t=1523524531745%3B1523582031695%3B1523585461629%3B2%3B17; _ym_isad=2; roybatty=TNI1625!AEJTbFLQJZ9lciit1wdEB6y7W6OS2yMXqxcVQaZLj9oFVaVTt72VEzWcRzG2U7hgsc8i9EoG4a1iVesHPbV%2FNS2S9%2BpYrXTF4VlNLxQGwPUCi5msTV3lrUzspfIqDrcInuWw27fVEogdon0J3o6Zu%2F9Mg0DMFEWkxulCZ1QBvR1V%2C1; TASession=%1%V2ID.B0F6C0EB0862EC85BC3125942CB1DB17*SQ.82*MC.16631*LR.https%3A%2F%2Fwww%5C.baidu%5C.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D1%26tn%3D97150107_hao_pg%26wd%3Dtripadvisor%26rsv_pq%3Ddfa1ece500046642%26rsv_t%3D7d11LN6xYVhclDXOJ0FkoGkjv351YAx%252BT1fbhbbi175pD01by9KjdmWjuZvU%252FXJHel3mogn%252F%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug3%3D4%26rsv_sug1%3D3%26rsv_sug7%3D100*LP.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*PR.427%7C*LS.DemandLoadAjax*GR.59*TCPAR.47*TBR.32*EXEX.22*ABTR.48*PHTB.21*FS.41*CPU.32*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.FDD01777AE3C8D12F28284FCA5F69F46*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.267031; TAUD=LA-1523582028433-1*RDD-1-2018_04_12*LG-16478870-2.1.F.*LD-16478871-....."
#
# }
#
# url_save = "https://www.tripadvisor.cn/Saves/all"
# sv_data = requests.get(url_save,headers=headers)
# soup = BeautifulSoup(sv_data.text,"lxml")
# print(soup)
#
# titles = soup.select("a.location_summary")
# print(titles)

