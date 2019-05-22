import pymysql
conn = pymysql.connect(host='172.16.10.71', port=3306, user='python_team', passwd='shiqiyu', db='hooli_school',charset="utf8")
#判断是否数据库里有该条数据
def judgeMS(dateDict=dict,conn=conn):
    cursor = conn.cursor()
    sql = "select * from JK_datebase WHERE url = '{}'".format(dateDict['url'])
    conn.ping(reconnect=True)
    cursor.execute(sql)
    result=cursor.fetchall()
    # conn.commit()
    conn.close()
    return result
#插入数据
def insertMysql(date,conn=conn):
    cursor = conn.cursor()
    conn.ping(reconnect=True)
    sql='insert into JK_datebase(url,university,programme,tuition_fee,overview,career,assessment,duration) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key UPDATE programme=%s,tuition_fee=%s,overview=%s,career=%s,assessment=%s,duration=%s'
    cursor.execute(sql,(date['url'],date['university'],date['programme'],date['fee'],date['overview'],date['career'],date['assessment'],date['duration'],date['programme'],date['fee'],date['overview'],date['career'],date['assessment'],date['duration']))
    conn.commit()
    conn.close()
    # return '插入新数据'
#比较数据
def compareMysql(date=dict,conn=conn):
    cursor = conn.cursor()
    conn.ping(reconnect=True)
    sql="select * from JK_datebase where url='%s'" % date['url']
    cursor.execute(sql)
    result=cursor.fetchone()
    newList=date.values()
    if result!=None:
        selList=list(result)
        differenceList=[n for n in newList if n not in selList]
        insertDiffrenceMysql(differenceList=differenceList,date=date)
        conn.commit()
        conn.close()
        # insertMysql(date=date)
    # return '比较新旧数据'
def insertDiffrenceMysql(differenceList,date,conn=conn):
    cursor = conn.cursor()
    if differenceList!=[]:
        #将该条数据插入变化表里
        text=[]
        for d in differenceList:
            for key,values in date.items():
                if values==d:
                    text.append(key)
        text=','.join(text)
        conn.ping(reconnect=True)
        diffSql = "insert into JK_change_eng(url,diffrence,university) VALUES (%s,%s,%s) on duplicate key UPDATE diffrence=%s"
        cursor.execute(diffSql,(date['url'],text,date['university'],text))
        conn.commit()
        # print(text)
        conn.close()