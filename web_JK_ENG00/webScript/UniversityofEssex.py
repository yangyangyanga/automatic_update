from middleware import *
makeThreading(school='University of Essex',urllist=getUrl(121),xpathDict={'fee':"//*[contains(text(),'International fee')]//following-sibling::*",'programme':'//*[@id="content"]//h1'})