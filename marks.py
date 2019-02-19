from bs4 import BeautifulSoup
import requests
import json


f = open('marks.html',"r")

materias = []
cnt = 0
sopa = BeautifulSoup(f, 'html.parser')
table = sopa.find("table",{'class':'oceny'})
subjects = table.find_all("tr")[1:]
for s in subjects:
    td = s.findChildren("td")
    name = td[0].text
    code = td[1].text
    mark = float(td[2].text.replace(",","."))
    typeOfMark = td[3].text
    teacher = td[6].text
    semester = td[7].text
    materias.insert(cnt,{"name":name,"code":code,"mark":mark,"type":typeOfMark,"teacher":teacher,"semester":semester})
    cnt+=1

with open("marks.json", "w") as fOut:
    json.dump(materias,fOut)

