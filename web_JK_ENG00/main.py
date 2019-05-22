import os,re

import sys
sys.path.append(r"D:\pycharm\automatic\automatic_update\web_JK_ENG00")
# import webScript
from webScript.sendEmail import *
print(os.getcwd()+"888888888888")
fileNameList=os.listdir(os.getcwd()+'\web_JK_ENG00\webScript')
fileNameList.remove('dateBase.py')
fileNameList.remove('middleware.py')
fileNameList.remove('sendEmail.py')
fileNameList.remove('__pycache__')
fileNameList=fileNameList[0:1]
# print(os.getcwd()+'\webScript')
# print(fileNameList)
for fNl in fileNameList:
    # print(fNl)
    print("**************************************** "+fNl)
    print("*******************11111********************* " + os.getcwd())
    fn='python '+os.getcwd()+'\web_JK_ENG00\webScript\\'+fNl
    print("======",fn)
    os.system('python '+os.getcwd()+'\web_JK_ENG00\webScript\\'+fNl)
    # f=open(os.getcwd()+'\webScript\\'+fNl,'r')
    # files=f.read()
    # print(files)
    # school=re.findall(r'school=[\'\"].*[\'\"]',files)
    # print(school)
    # f.close()
SendEmailMain()

