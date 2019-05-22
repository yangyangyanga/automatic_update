# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql,datetime,difflib
class JkAuPipeline(object):
    conn = pymysql.connect(host='172.16.10.71', user='python_team', passwd='shiqiyu', db='hooli_school', charset='utf8')
    cursor = conn.cursor()
    def process_item(self, item, spider):
        try:
            print("正在写入数据====================")
            if self.judgeMS(item)==():
                self.insertMysql(item)
            else:
                self.compareMysql(item)
        except Exception as e:
            self.conn.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.conn.close()
        return item
    def judgeMS(self,item):
        sql = "select old_id from monitor WHERE old_id = '%s'" % item['old_id']
        self.conn.ping(reconnect=True)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.conn.commit()
        return result
    def insertMysql(self,item):
        self.conn.ping(reconnect=True)
        date = item
        # 表未定，暂时省略部分内容
        sql = "insert into monitor(old_id,major_name,degree_name,web_label,web_content,state_code,url_now,url_old,update_time,university) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " \
              "on duplicate key update web_label=%s,web_content=%s,state_code=%s,url_now=%s,update_time=%s"
        self.cursor.execute(sql, (
            item['old_id'], item['major_name_en'], item['degree_name'], item['web_label'], item['web_content'],
            item['state_code'],
            item['url_now'], item['url_old'], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), item['university'],
            item['web_label'], item['web_content'], item['state_code'],
            item['url_now'], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.conn.commit()
    def compareMysql(self,item):
        self.conn.ping(reconnect=True)
        sql = "select web_label,web_content from monitor where old_id='%s'" % item['old_id']
        self.cursor.execute(sql)
        self.conn.commit()
        results = self.cursor.fetchall()
        # print(len(results[0]))
        # print(results)
        d = difflib.Differ()
        diff_la = d.compare(item['web_label'], results[0][0])
        diff_co = d.compare(item['web_content'], results[0][1])
        change_la = '\n'.join(list(diff_la))[0].replace(' ', '0').replace('-', '1').replace('+', '1').replace('?', '1')
        change_co = '\n'.join(list(diff_co))[0].replace(' ', '0').replace('-', '1').replace('+', '1').replace('?', '1')
        # print(change_la)
        # print(change_co)
        change_context = change_la + change_co
        sqls = "update monitor set update_time=%s,change_context=%s,web_label=%s,web_content=%s where old_id=%s"
        self.cursor.execute(sqls, (item['update_time'],
        change_context, item['web_label'], item['web_content'], item['old_id']))
        self.conn.commit()
