from middleware import *
makeThreading(school='University of Aberdeen',urllist=getUrl(139),xpathDict={'programme':'//*[@id="top"]/div[3]/div/h1','fee':"//*[contains(text(),'International Students')]//following-sibling::*"})