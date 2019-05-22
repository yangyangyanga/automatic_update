from middleware import *
urls=getUrl(146)
makeThreading(urllist=urls,school='Aberystwyth University',xpathDict={'programme':'//h1/text()'})
