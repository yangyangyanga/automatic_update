from middleware import *
makeThreading(school='University of Huddersfield',urllist=getUrl(164),xpathDict={'programme':'//h1//text()','fee':'//p[contains(text(),"￡")]'})