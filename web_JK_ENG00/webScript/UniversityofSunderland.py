from middleware import *
makeThreading(school='University of Sunderland',urllist=getUrl(195),xpathDict={'fee':"//*[contains(text(),' International fee')]//*|//*[contains(text(),'Tuition fee')]//*",'programme':'/html/body/div[2]/header/div/div[1]/h1/span[1]'})