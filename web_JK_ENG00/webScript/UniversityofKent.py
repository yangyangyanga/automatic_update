from middleware import *
makeThreading(school='University of Kent',urllist=getUrl(130),xpathDict={'programme':'//h1//text()','fee':'//*[@id="funding"]/table/tbody/tr[1]/td[3]'})