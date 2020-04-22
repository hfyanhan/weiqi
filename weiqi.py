import sqlite3
import requests
from funcnetio import *
from datetiqu import date
from datebase import comm
from datebasec import *

url="http://iwdb.cn/game/search/"
if not isexist("1.config"):
    fc=open("1.config",mode="w",encoding="utf-8")
    fc.close()
fr=open("1.config",mode="r",encoding="utf-8")
#fr.write(' ')
w=fr.read()
fr.close()

cre=sqlite3.connect("weiqi.db")
cur=cre.cursor()
if w=='':
    cretet(cre)
    wrhtml('0',1,1,'config')
    
    
i=int(wrhtml('',1,2,'config'))
flag=0
while flag!=77:
   if i % 500==0:
       wrhtml(str(i),1,1,'config')
       print(i)
       cre.commit()
   flag=comm(date(getc(url+str(i),0.2,0,{},{})),cur)
   i=i+10
cre.commit()
cre.close()


