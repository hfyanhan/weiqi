import sqlite3

order=['name','place','time','white','black','rule','tiehuan','result','fromb']
orderb=['id','name','place','time','result','tiehuan','white','black','fromb','fb','rule']
dict={
    'place':'PC',
    'time':'DT',
    'name':'EV',
    'white':'PW',
    'black':'PB',
    'rule':'RU',
    'tiehuan':'KM',
    'fromb':'SO',
    'result':'RE'
}

def crez(cre):
    e=cre.cursor()
    e.execute('''CREATE TABLE weiqi(id char(18) PRIMARY KEY,date text);''')
    cre.commit()

def hb(w):
    stra="(;AP[iwdb.cn]"
    for info in order:
        if w[info]=='':
            continue
        stra=stra+dict[info]+"["+w[info]+"]"
    w['fb']=w['fb']+" "
    stra=stra+w['fb'][1:-1]
    return stra

def dih(item):
    a={}
    i=0
    for info in orderb:
        a[info]=item[i]
        if a[info]==None:
            a[info]=''
        i=i+1
    return a

cre=sqlite3.connect("up-data.db")
#crez(cre)
e=cre.cursor()
cre_old=sqlite3.connect("weiqi.db")
ol=cre_old.cursor()
a=ol.execute("select id,name,place,time,result,tiehuan,white,black,fromb,fb,rule from weiqi;")
i=0
for item in a:
    a=[item[0]]
    a.append(hb(dih(item)))
    e.execute('''INSERT INTO weiqi(id,date)values(?,?)''',a)
    i=i+1
    if i%100==1:
        print(i)
cre.commit()
cre_old.close()
cre.close()

#print(hb(t))