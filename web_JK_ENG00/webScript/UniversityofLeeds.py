from middleware import *
makeThreading(school='University of Leeds',urllist=getUrl(109),xpathDict={'programme':'//*[@id="main"]/div/header/h1','fee':"//*[contains(text(),'International fees')]//following-sibling::*[1]|//*[@id='acc3']"})