from middleware import *
makeThreading(school='University of St Andrews',urllist=getUrl(102),xpathDict={'programme':'//section/h2/text()','fee':'//*[contains(text(),"Tuition fees")]/following-sibling::p//text()'})