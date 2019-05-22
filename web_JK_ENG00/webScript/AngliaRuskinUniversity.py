from middleware import *
makeThreading(urllist=getUrl(212),school='Anglia Ruskin University',xpathDict={'programme':'//h1/text()','fee':'//div[@id="feesfunding"]//text()'})