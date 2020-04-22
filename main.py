
from flask import Flask,request,redirect,render_template,session,url_for,make_response,abort,flash
import sqlite3

Dict4={
    'tiehuan':'贴还',
    'black':'执黑',
    'white':'执白',
    'time':'时间',
    'name':'名称',
    'place':'地点',
    'result':'结果',
    'fromb':'来源',
    'rule':'规则'
}
orderh=['name','place','time','result','tiehuan','white','black','fromb','rule']
orderb=['id','name','place','time','result','tiehuan','white','black','fromb','fb','rule']
order=['name','place','time','white','black','rule','tiehuan','result','fromb']
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
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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


@app.route('/<type>')
def small(type):
    file=type+".html"
    return render_template(file)



@app.route('/game/search',methods=['GET','POST'])



@app.route('/game/search/<start>',methods=['GET','POST'])

def search(start):
    start=int(start)
    cre=sqlite3.connect("weiqi.db")
    e=cre.cursor()
    a=e.execute("select id,name,place,time,result,tiehuan,white,black,fromb,fb,rule from weiqi;")
    ten=[]
    j=0
    for b in a:
        j=j+1
        if j<start or j>start+10:
            continue
        q={}
        i=0
        for info in orderb:
            q[info]=b[i]
            if q[info]==None:
                q[info]=''
            i=i+1
        ten.append(q)
    return render_template('search.html',ten=ten,dicta=Dict4,order=orderh)

@app.route('/replay/view/<id>')
def view(id):
    return render_template('view.html',id=id)


@app.route('/welcome/get/<id>')
@app.route('/game/down/<id>')
@app.route('/replay/get/<id>')
def get(id):
    w=[];
    w.append(id)
    cre_old=sqlite3.connect("weiqi.db")
    ol=cre_old.cursor()
    a=ol.execute("select id,name,place,time,result,tiehuan,white,black,fromb,fb,rule from weiqi where id=?;",w)
    for t in a:
        item=t
    stra=hb(dih(item))
    cre_old.close()
    return stra
    



app.run(debug=False,host='0.0.0.0',port=8080)