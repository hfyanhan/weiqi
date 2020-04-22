import sqlite3
from funcsq import *

order=['id','name','place','time','result','tiehuan','white','black','fromb','fb','rule']

def comm(date,e):
    for item in date:
        d=[]
        for con_name in order:
            d.append(item[con_name])
        s="insert into weiqi"
        s=s+'''(id,name,place,time,result,tiehuan,white,black,fromb,fb,rule)
				   values(?,?,?,?,?,?,?,?,?,?,?)'''
        try:
            e.execute(s,d)
        except BaseException:
            if checkjl(e,'weiqi',"d[0]","id"):
                return 66
            print(d)
            return 77
    return 0