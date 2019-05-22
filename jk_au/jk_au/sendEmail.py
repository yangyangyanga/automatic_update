import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import pymysql
def sendEmail(subject='无标题',messageText='无内容'):
    # accepter = 'zjlhyd0422@163.com'
    accepter = "625786425@qq.com"
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
    sql = "select old_id,url_old,university,change_context from Label_content where old_id like 'a%' and change_context like '%1%' order by university"
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.commit()
    sql2 = "select count(*),university from Label_content where change_context like '%1%' and old_id like 'a%' GROUP BY university"
    cursor.execute(sql2)
    conn.commit()
    result2=cursor.fetchall()
    # print(result)
    # print(result2)
    conn.close()
    sendemailschool=''.join(list(map(lambda x:x[1]+'有'+str(x[0])+'条专业发送变化'+'\n',result2)))
    sendemaillists=''.join(list(map(lambda x:'id为: '+x[0]+' 的专业'+x[3].replace('01','内容发生变化').replace('11','内容和标签发生变化').replace('10','标签发生变化')+' 学校: '+x[2]+' 链接为:'+x[1]+'\n',result)))
    messagetext=sendemailschool+'\n'+sendemaillists
    if messagetext!='\n':
        sendEmail(subject='澳洲变化邮件',messageText=messagetext)
# SendEmailMain()

