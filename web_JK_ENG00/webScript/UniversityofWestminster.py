from middleware import *
makeThreading(school='University of Westminster',urllist=getUrl(206),xpathDict={'programme':'/html/body/div[2]/div[2]/div/header/h1/text()','fee':'/html/body/div[4]/div/section/div[2]/div[2]/div/div[2]/div[1]/div[2]/span[2]/a'})