from middleware import *
makeThreading(school='University College London',urllist=getUrl(106),xpathDict={'programme':'//h1//text()','fee':'//*[contains(text(),"£")]//text()'})