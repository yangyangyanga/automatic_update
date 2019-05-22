# -*- coding: utf-8 -*-
import scrapy
import pymysql,re,time
from jk_ca.items import JkCaItem,get_item
from decimal import *
from jk_ca.middlewares import remove_class,clearallSB,runSelenuim
class SchoolJkSpiderSpider(scrapy.Spider):
    name = 'school_jk_spider'
    # allowed_domains = ['a.b']
    handle_httpstatus_list = [301, 302, 204, 206, 404, 500]
    start_urls = ['http://www.baidu.com/']
    def parse(self, response):
        school_list=self.get_school_id()[0]
        id_lists=self.get_school_id()[1]
        for sl,il in zip(school_list,id_lists):
            # print(sl,il)
            results=self.get_url_id(sl)
            # print(results)
            n=0
            for r in results:
                # print(n)
                time.sleep(0.1)
                if n==25:
                    runSelenuim(r[0])
                n = n + 1
                runNum=n/len(results)
                rN = str(runNum)[0:5]
                # print(rN)
                rN = float(rN) * 100
                rN = Decimal(rN).quantize(Decimal('0.00'))
                cout = ('正在监控' + 'id为 ' + r[1] + ' 的专业名、学位类型、课程时长等字段，学校:' + sl + ' 进度:' + str(rN)[0:5] + '%')
                print(cout)
                with open('Canadafileout.txt', 'a+', encoding='utf-8') as fi:
                    fi.write(cout + '\n')
                yield scrapy.Request(dont_filter=True,url=r[0],callback=self.parse_main,meta={'url':r[0],'sid':str(r[1]),'degree_name':r[2],'major_name_en':r[3],'school_name':sl})
    def parse_main(self,response):
        item=get_item(JkCaItem)
        # print(item)
        item['url_now']=response.url
        item['url_old']=response.meta['url']
        item['old_id']=response.meta['sid']
        item['degree_name']=response.meta['degree_name']
        item['major_name_en']=response.meta['major_name_en']
        item['university']=response.meta['school_name']
        item['state_code']=response.status
        print(response.status)
        # print(response.text)
        content=clearallSB(remove_class(response.text))
        biaoqian=remove_class(re.findall(r"<[\w\W\?]*?>",remove_class(response.text)))
        # print(biaoqian)
        content=''.join(re.sub(r'<[\w\W\?]*?>','',content))
        # print(content)
        item['web_label']=biaoqian
        item['web_content']=content
        # print(item)
        yield item
    def get_school_id(self):
        conn = pymysql.connect(host='47.94.152.221', port=3306, user='chaxun', passwd='chaxun', db='hooli_study_gather',
                               charset='utf8')
        conn.ping(reconnect=True)
        cursor = conn.cursor()
        sql = "select ename,id from school_info where country_id=4"
        cursor.execute(sql)
        conn.commit()
        results = cursor.fetchall()
        conn.close()
        school_lists = list(map(lambda x: x[0], list(results)))
        id_lists = list(map(lambda x: x[1], list(results)))
        return school_lists,id_lists
    def get_url_id(self,school):
        # 连接数据库
        conn = pymysql.connect(host='47.94.152.221', port=3306, user='chaxun', passwd='chaxun', db='hooli_study_gather',
                               charset='utf8')
        conn.ping(reconnect=True)
        cursor = conn.cursor()
        selu = 'select url,id,degree_name,major_name_en from tmp_school_ca_ben where school_name="%s"' % school
        # 取出本科数据
        cursor.execute(selu)
        resultu = cursor.fetchall()
        resultu = list(map(lambda x: [x[0], 'cu' + str(x[1]),x[2],x[3]], resultu))
        # print(resultu)
        selp = 'select url,id,degree_name,major_name_en from tmp_school_ca_college where school_name="%s"' % school
        # 取出研究生数据
        cursor.execute(selp)
        resultp = cursor.fetchall()
        resultp = list(map(lambda x: [x[0], 'cu' + str(x[1]),x[2],x[3]], resultp))
        # conn.close()
        # print(resultp)
        result = resultu + resultp
        # print(result)
        conn.close()
        return result
