from middleware import *
makeThreading(school='Cardiff University',urllist=getUrl(134),xpathDict={'programme':'//*[@id="content"]/div[1]/div/div[1]/h1','fee':'//*[@id="tuitionfees"]/table/tbody/tr/td[1]'})