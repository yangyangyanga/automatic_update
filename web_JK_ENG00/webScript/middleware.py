from lxml import etree
import threading,requests,re
from queue import LifoQueue
from dateBase import *
#在数据库中获取连接
def getUrl(sid):
    conn = pymysql.connect(host='172.16.10.71', port=3306, user='python_team', passwd='shiqiyu', db='hooli_study_gather',charset="utf8")
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql1="select DISTINCT url from tmp_school_uk_ben where sid='%s'" %sid
    conn.ping(reconnect=True)
    cursor.execute(sql1)
    result1 = cursor.fetchall()
    sql2="select DISTINCT url from tmp_school_uk_yan where sid='%s'" %sid
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    conn.close()
    result=result1+result2
    cout=list(map(lambda x: ''.join(x),list(result)))
    return cout
#将详情页的链接放在队列里
def urlQueue(urlList):
    urlQue=LifoQueue()
    for uL in urlList:
        urlQue.put(uL)
    return urlQue.queue
#访问详情页，xpathDict是要监控的字段的xpath字典，key是字段名，键是xpath
def getProgram(url,xpathDict={'none':None},school=''):
    response=etree.HTML(requests.get(url).content)
    print('正在监控  '+school+'  中...')
    #要监控的字段
    coutDict={'url':url,'university':school,'programme': '', 'fee': '', 'overview': '', 'career': '','assessment': '', 'duration': ''}
    for key,value in zip(xpathDict.keys(),xpathDict.values()):
        if key!=None and value!=None:
            try:
                coutDict[key]=remove_class(response.xpath(value))[0:255]
            except:
                pass
    # a=judgeMS(dateDict=coutDict)
    # return a
    if judgeMS(coutDict)==():
        a=insertMysql(date=coutDict)
    elif judgeMS(coutDict)!=():
        b=compareMysql(date=coutDict)
    return coutDict
#创建线程,urllist是要访问的链接，threadingNum是要开启的线程数量
def makeThreading(urllist,xpathDict,school):
    # programmeThreading = threading.BoundedSemaphore(threadingNum)
    for i in urllist:
        # t = threading.Thread(target=runThreading,args=(i,programmeThreading,xpathDict,school))
        # t.start()
        getProgram(i,xpathDict=xpathDict,school=school)
#运行线程
def runThreading(programmeUrl,programmeThreading,xpathDict,school):
    programmeThreading.acquire()
    gP=getProgram(url=programmeUrl,xpathDict=xpathDict,school=school)
    print('访问'+school+' '+programmeUrl)
    programmeThreading.release()
# header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',}
# def newMakeThread(threadingNum):
#     threads = []
#     for i in range(1,threadingNum):
#         threads.append(i)

def remove_class(var):
    var=''.join(var)
    #清洗标签
    clear_class=re.findall('[a-zA-Z\-]+=[\'\"][a-zA-Z0-9\-/\)\(\.\s\;\:\`\~\@\!\#\$\%\^\&\*\_\+\=\,\?\{\}]*[\'\"]', var)
    for i in clear_class:
        var=var.replace(' ' + i, '')
    #去除a标签
    var = var.replace('<a>', '').replace('</a>', '')
    #去除注释
    fan_ren_de_biao_qian=re.findall('<!.+>',var)
    for i in fan_ren_de_biao_qian:
        var=var.replace(i,'')
    var=clear_same_s(var)
    return var
def clear_same_s(strs):
    strs=''.join(strs).replace("\r", "").replace('\t', "")
    fan_ren_de_kong_ge=re.findall('  ',strs)
    if fan_ren_de_kong_ge !=[]:
        for i in fan_ren_de_kong_ge:
            strs=strs.replace(i,'')
    strs=strs.split('\n')
    while '' in strs:
        strs.remove('')
    strs='\n'.join(strs)
    return strs