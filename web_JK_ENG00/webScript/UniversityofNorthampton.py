from middleware import *
makeThreading(school='University of Northampton',urllist=getUrl(196),xpathDict={'programme':'//*[@id="site-content"]/article/header/div[2]/h1/text()','fee':'//*[@id="fees-and-funding"]'})