import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import pymysql
def sendEmail(subject='无标题',messageText='无内容'):
    accepter = 'zjlhyd0422@163.com'
    # accepter = "cyh6257@163.com"
    sender = "cyh6257@163.com"
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(messageText, 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = accepter
    #邮件标题subject
    subject = subject
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com', '25')
        smtp.login('cyh6257@163.com', 'cyh1995')
        smtp.sendmail(sender,accepter, message.as_string())
        print("发送成功")
        smtp.quit()
    except smtplib.SMTPException as e:
        print(e, "发送失败")
def SendEmailMain():
    conn = pymysql.connect(host='172.16.10.71', port=3306, user='python_team', passwd='shiqiyu', db='hooli_school',charset="utf8")
    cursor = conn.cursor()
    #获取变化的学校数据
    conn.ping(reconnect=True)
    sql = 'select * from JK_change_eng order by university'
    cursor.execute(sql)
    result=cursor.fetchall()
    # print(result)
    #获取变化的学校名
    sel2='select university from JK_change_eng group by university'
    cursor.execute(sel2)
    result2=cursor.fetchall()
    result2=list(result2)
    result2=list(map(lambda x:list(x)[0],result2))
    # print(result2)
    conn.close()
    for r2 in result2:
        schoolIndex=getIndex(r2,result)
        if len(schoolIndex)==1:
            SendEmailContent='  '.join(result[schoolIndex[0]])
            sendEmail(subject=r2+'发生变化',messageText=SendEmailContent)
        else:
            schoolIndex=list(map(int,schoolIndex))
            SendEmailList=result[min(schoolIndex):max(schoolIndex)+1]
            SendEmailList=''.join(list(map(lambda x:'  '.join(x)+'\n',SendEmailList)))
            sendEmail(subject=r2+'发生变化',messageText=SendEmailList)
def getIndex(uname,resu):
    index=[]
    for re in resu:
        if re[0]==uname:
            index.append(resu.index(re))
    return index
