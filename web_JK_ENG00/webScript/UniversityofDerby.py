from middleware import *
makeThreading(school='University of Derby',urllist=getUrl(180),xpathDict={'programme':'//h1/strong','fee':"//*[contains(text(),'International fee')]//following-sibling::*"})