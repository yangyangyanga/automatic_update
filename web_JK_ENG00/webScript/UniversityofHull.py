from middleware import *
makeThreading(school='University of Hull',urllist=getUrl(176),xpathDict={'programme':'//*[@id="main-content"]/header/div[2]/div[1]/h1|//*[@id="main-content"]/section[1]/div[2]/div/div/h1','fee':"//*[contains(text(),'Fees and funding')]//following-sibling::*"})