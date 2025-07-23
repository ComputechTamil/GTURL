
def gturl(url:str):
    """url:tamilyogi.vip or tamilyogi/s?=something"""
    #keyword=keyword.lower().replace(" ","+")
    slash_index = url.find("/")
    domain=url[:slash_index].replace(".","-")
    remain_path=url[slash_index+1:]
    return "https://"+domain+".translate.goog/"+remain_path+"&_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en-US&_x_tr_pto=wapp"
def gtrequest(url:str):
    gturl(url)
def gtsearch(string:str):
    pass
##print(gturl("torrentz2.nz/search?q=good night"))
##print(gturl("tamilyogi.vip/?s=good night"))
##print(gturl("www.1tamilblasters.tel/index.php?/search/&q=Parking&search_and_or=and"))
