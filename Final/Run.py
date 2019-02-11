import json
import unicodedata
flist=['Format.json']
l=[]

for col in flist:
  result=""
  html="<table class='table'>"
  exp=0
  act=0
  f = open(col,'r')
  ip = f.read()
  json_data = json.loads(ip)
  test_data = json_data['Test_Data']
  key_set = test_data[0].keys()
  for key in key_set:
    html += "<th>"+key+"</th>"
  html+="<th>""Results""</th>"
  html+="<th>""Status""</th>"
  for ij in range(0,len(test_data)):
      l.append(test_data[ij].values())
  for i in l:
    html+="<tr>"
    
    co=0
    id=0
    for j in i:
      html+="<td id='"+str(id)+"'>"+str(j)+"</td>"
      id=id+1
      co=co+1
      if(co==2):
        exp=j
      elif(co==3):
        act=j
    print(exp,act)
    if(exp==act):
      print("Pass")
      result="Pass"
    else:
      result="Fail"
    html+="<td>"+str(result)+"</td>"
    if(result=="Pass"):
      html+="<td bgcolor='Green'>""</td>"
    elif(result=='Fail'):
      html+="<td bgcolor='Red'>""</td>"
      html+="</tr>"
  with open("index.html", "a") as myfile:
    myfile.write(str(html))
html1="</table>"
html1+="<div id='piechart'></div>"
with open("index.html", "a") as myfile:
    myfile.write(str(html1))
      
print(html)
  
      
      
      
      
