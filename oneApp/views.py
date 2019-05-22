from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.core.paginator import Paginator
import os
from .models import Monitor_copy1


# Create your views here.
# 首页选择需要监控的国家
def index(request):
    # return HttpResponse("Hi 我是首页")
    # if request.session.get('shishixinxi') is None:
    #     request.session['shishixinxi'] = "没有session"
    return render(request, 'oneApp/index.html')


def click_England(request):
    # return HttpResponse("Hi 我是首页111111111111111111111")
    print("===========================", os.getcwd()+r'\jk_en\main.py')
    # if country == "England":
    os.system('python '+os.getcwd()+r'\jk_en\main.py')
    # elif country == "Australia":
    #     os.system('python ' + os.getcwd() + '\jk_au\main.py')
    return redirect(reverse('oneApp:index'))
    # return HttpResponse("Hi 正在监控英国学校。。。。。。。。")

def click_Australia(request):
    print("===========================", os.getcwd()+r'\jk_au\main.py')
    os.system('python ' + os.getcwd() + r'\jk_au\main.py')
    return redirect(reverse('oneApp:index'))

def click_Canada(request):
    print("===========================", os.getcwd()+r'\jk_ca\main.py')
    os.system('python ' + os.getcwd() + r'\jk_ca\main.py')
    return redirect(reverse('oneApp:index'))

# 查看监控结果页面后台逻辑
def show_result(request, country, up):
    # 获取monitor_copy1中的学校数据：404、403、200、200
    # monitor_copy1 = Monitor_copy1.objects.all()
    # print("monitor_copy1: ", monitor_copy1)
    print("country: ", country)

    # 根据开头包含的关键字区分各个国家以及本研
    old_id__startswithU = ''
    old_id__startswithP = ''
    if country == "England":
        old_id__startswithU = 'eu'
        old_id__startswithP = 'ep'
    elif country == "Australia":
        old_id__startswithU = 'au'
        old_id__startswithP = 'ap'
    elif country == "Canada":
        old_id__startswithU = 'cu'
        old_id__startswithP = 'cp'
    elif country == "American":
        old_id__startswithU = 'mu'
        old_id__startswithP = 'mp'
    print("old_id__startswithU: ", old_id__startswithU)
    print("old_id__startswithP: ", old_id__startswithP)

    dataDictU = getData(Monitor_copy1, old_id__startswithU)
    print("dataDictU: ", dataDictU)

    dataDictP = getData(Monitor_copy1, old_id__startswithP)
    print("dataDictP: ", dataDictP)

    contextdict = {}
    contextdict['country'] = country
    contextdict['undergraduate'] = dataDictU
    contextdict['postgraduate'] = dataDictP
    # contextdict = dict(dataDictU, **dataDictP, **{'country': country, "old_id__startswithU": old_id__startswithU, "old_id__startswithP": old_id__startswithP})
    if up == "ug":
        contextdict['up'] = "本科"
    else:
        contextdict['up'] = "研究生"
    print(contextdict)
    return render(request, 'oneApp/show.html', context=contextdict)


# 解析获取各个状态的数据
# 获取monitor_copy1中的学校数据：404、403、200、200
def getData(Monitor_copy1, old_id__startswith):
    dataDict = {}

    # 页面链接失效(404)的数量
    data404 = Monitor_copy1.objects.filter(state_code=404,old_id__startswith=old_id__startswith)
    data404count = data404.count()
    print("data404count==", data404count)
    dataDict['data404number'] = data404count

    # 获取存在404页面的学校名称，存为一个列表
    university404 = []
    if data404.exists():
        for d in data404:
            university404.append(d.university)
            # print(d.university)
    else:
        # 没有数据的情况显示为无
        university404.append("无")
    university404 = list(set(university404))
    dataDict['data404university'] = university404

    # 页面禁止访问(403)的数量
    data403 = Monitor_copy1.objects.filter(state_code=403,old_id__startswith=old_id__startswith)
    data403count = data403.count()
    print("data403count==", data403count)
    dataDict['data403number'] = data403count
    # 获取存在403页面的学校名称，存为一个列表
    university403 = []
    if data403.exists():
        for d in data403:
            university403.append(d.university)
            # print(d.university)
    else:
        university403.append("无")
    university403 = list(set(university403))
    dataDict['data403university'] = university403


    # 页面(200)的数量
    data200 = Monitor_copy1.objects.filter(state_code=200,old_id__startswith=old_id__startswith)
    data200count = data200.count()
    print("data200count==", data200count)

    structure200 = []
    content200 = []
    if data200.exists():
        for d in data200:
            # 判断页面是结构变化，以下四个字段全为空
            if d.major_name is None and d.degree_name is None and d.tuition_fee is None and d.duration is None:
                structure200.append(d.university)
            else:
                content200.append(d.university)
            # content200.append('哈哈哈')

    dataDict['dataStructure200number'] = len(structure200)
    if len(structure200) == 0:
        structure200.append("无")
    dataDict['dataStructure200university'] = list(set(structure200))
    dataDict['dataContent200number'] = len(content200)
    if len(content200) == 0:
        content200.append("无")
    dataDict['dataContent200university'] = list(set(content200))

    return dataDict


# 读取monitor_copy1表数据
def get_monitor_copy1_data(request, country, pageid):
    # 展示字段
    # id、 old_id、 major_name、 degree_name、 tuition_fee、 duration、 state_code、 url_now、 url_old、 university、 update_time、 sid
    # 所有专业数据
    # monitor_copy1 = Monitor_copy1.objects.all()
    print("get_country_key(country).get('old_id__startswithCountry'): ", get_country_key(country))
    monitor_copy1 = Monitor_copy1.objects.filter(old_id__startswith=get_country_key(country).get('old_id__startswithCountry'))
    paginator = Paginator(monitor_copy1, 10)
    page = paginator.page(pageid)
    return render(request, 'oneApp/showtable.html', context={"monitor_copy1": page, 'country': country})
    # return HttpResponse("Hi 正在展示学校数据。。。。。。。。")

# 根据开头包含的关键字区分各个国家
def get_country_key(country):
    old_id__startswithCountry = ''  # 国家
    old_id__startswithU = ''        # 本科
    old_id__startswithP = ''        # 研究生
    if country == "England":
        old_id__startswithCountry = 'e'
        old_id__startswithU = 'eu'
        old_id__startswithP = 'ep'
    elif country == "Australia":
        old_id__startswithCountry = 'a'
        old_id__startswithU = 'au'
        old_id__startswithP = 'ap'
    elif country == "Canada":
        old_id__startswithCountry = 'c'
        old_id__startswithU = 'cu'
        old_id__startswithP = 'cp'
    elif country == "American":
        old_id__startswithCountry = 'm'
        old_id__startswithU = 'mu'
        old_id__startswithP = 'mp'
    return {"old_id__startswithCountry": old_id__startswithCountry, "old_id__startswithU": old_id__startswithU, "old_id__startswithP": old_id__startswithP}


# 获取监控时的实时信息
from django.http import JsonResponse
def shishixinxi(request, country):
    with open(os.getcwd() + "\\"+country+"fileout.txt", 'r', encoding='utf-8') as f:
        last_line = f.readlines()
        # print("last_line: ", last_line)
        # request.session['shishixinxi'] = last_line
    return JsonResponse({"shishixinxi": last_line})
