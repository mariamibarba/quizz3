import json
import requests


city=input("შეიყვანეთ ქალაქის დასახელება:")

key='4f68fbf1843d0a8578ba43d49ff3ff02'
payload={'q':city,'appid': key,'units':'metric'}

r=requests.get('http://api.openweathermap.org/data/2.5/weather',params=payload)
print(r.text)
print(r.headers)
res=r.json()
print(res['coord'],['weather'])
ress=json.loads(r.text)
print(ress)
print(json.dumps(ress,indent=4))

with open ('data.json','w') as f:
    json.dump(res,f,indent=4)


a='ტემპერატურა:', ress['main']['temp'],'c'
b='ტენიანობა:',ress['main']['humidity'],'%'
print(a)
print(b)




