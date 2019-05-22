from middleware import *
urls=getUrl(145)
makeThreading(urllist=urls,school='Aston University',xpathDict={'programme':'//h1//text()','fee':'//strong[contains(text(),"uition")]/../text()'})