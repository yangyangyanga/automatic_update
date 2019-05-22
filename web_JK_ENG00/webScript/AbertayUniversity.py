from middleware import *
makeThreading(school='Abertay University',urllist=getUrl(197),xpathDict={'fee':'//h4[text()="International Students"]/../following-sibling::div/text()'})
