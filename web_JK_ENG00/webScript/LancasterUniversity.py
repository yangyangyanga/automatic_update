from middleware import *
makeThreading(school='Lancaster University',urllist=getUrl(105),xpathDict={'programme':'//h1//text()','fee':'//*[@id="fees"]/div/div/table/tbody/tr[3]/td[1]'})