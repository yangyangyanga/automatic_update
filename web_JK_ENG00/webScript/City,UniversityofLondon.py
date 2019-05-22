from middleware import *
makeThreading(urllist=getUrl(175),school='City, University of London',xpathDict={'fee':'//span[contains(text(),"£")]//text()'})