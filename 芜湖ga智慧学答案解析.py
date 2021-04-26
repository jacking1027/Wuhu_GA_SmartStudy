import requests,json

ip='http://60.167.58.178:8000'
getid='/zhjypt/app/getDjPageList'

print('芜湖ga智慧学答案分析v1.1\n')
print('请输入需要的答案序号：1，每周一考；2，每月一考；3，季度考试。')
a=input()

if a=='1':
    tp='mzyk'
    bc='KS_MZ'
elif a=='2':
    tp='myyk'
    bc='KS_MY'
elif a=='3':
    tp='jdks'
    bc='KS_JD'
else:
    quit()


data={
    'userId':'15377',
    'pageNo':'1',
    'type':tp,
    'bkCode':bc
}

ss=requests.session()
r1=ss.post(ip+getid,data=data)
ss.close()

ksid=json.loads(r1.text)['data']['rows'][0]['ID']

getda='/zhjypt/app/getKj'

r2=ss.post(ip+getda,data={'ksId':ksid})

jj=json.loads(r2.text)

c=0
for i in jj['data']['tmList']:
    c=c+1
    print(str(c)+'.'+i['NR'])
    for j in i['XXMX']:
        if j.get('sfzqda'):
            if j['sfzqda']=="1":print(j['xxbh']+'.'+j['xxnr'])
        else:
            if j['lx']=="2":print(j['nr'])

    print()

input()
