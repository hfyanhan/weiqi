from bs4 import BeautifulSoup
from funcnetio import *
Dict={
    '贴还':'tiehuan',
    '执黑':'black',
    '执白':'white',
    '时间':'time',
    '名称':'name',
    '地点':'place',
    '结果':'result',
    '来源':'fromb',
    '规则':'rule'
}
def guolv(a):
    b=""
    for cha in a:
        if cha=="\n" or cha=="\t":
            continue
        b=b+cha
    return b
def date(tes):
    a=""
    ans=[]
    bs1=BeautifulSoup(tes,"html5lib")
    for ju in bs1.find_all('div',{"class":"tbl-game-wrapper"}):
        item={}
        item['fb']=ju.div.div.div.div.div.a.div.get('data-jqi-diagram')#提取棋局
        item['id']=ju.div.div.div.div.div.a.get('href')+' '
        item['id']=item['id'][13:-1]
        for info in Dict.values():
            item[info]=''
        #print(item['id'])
        for info in ju.find_all('div',{'class':'tbl-gameinfo-item'}):
            name=info.find('div',{'class':'tbl-gameinfo-item-left'}).get_text()
            context=info.find('div',{'class':'tbl-gameinfo-item-right'}).get_text()
            name=guolv(name)
            context=guolv(context)
            item[Dict[name]]=context
        ans.append(item)
    return ans
#date(wrhtml('',1,2,'html'))