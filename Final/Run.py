
import json
import unicodedata
flist=['Format.json']
l=[]
for col in flist:
  result=""
  html=""
  exp=0
  act=0
  f = open(col,'r')
  ip = f.read()
  json_data = json.loads(ip)
  test_data = json_data['Test_Data']
  key_set = test_data[0].keys()
  for i in test_data[0].values():
    l.append(i)
  exp=l[1]
  act=l[2]
  if(exp==act):
    result= True
    r="pass"
  
  else:
    result=False
    r="Fail"
  
  html="<table class='table'><tr>"
  total_rec = len(test_data)
  for key in key_set:
    html += "<th>"+key+"</th>"
  html+="<th>""results""<th>"
  html+="<th>""ColorCode""<th>"
  html+="</tr>"

  html+="<tr id='somerow'>"
  j=0
  for i in range (0, len(test_data)):
    for key in key_set:
      
      html+="<td id ='"+str(j)+"'>"+str(test_data[i][key])+"</td>"
      j=j+1
  html+="<td>"+r+"</td>"
  if(result==False and r=='Fail'):
    html+="<td bgcolor='black'>""</td>"
  else:
    html+="<td bgcolor='pink'>""</td>"
  html+="</tr>"
  

  html+="</table>"
  html+="<div id='piechart'></div>"
  print(html)
  with open("index.html", "a") as myfile:
      myfile.write(str(html))


