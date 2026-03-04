
'''
with open('sample.json','w')as file:
    file.write('anvika')



     
with open('sample.json','a')as file:
    file.write('anvika')



with open('sample.json','r')as file:
    content =file.read()
    print(content)
    
    
import csv

with open ('excel.csv','r') as file :
    data=csv.reader(file)
    for row in data:
        print(row[1])


import csv

with open ('excel.csv','a',newline='\n') as file :
    data=csv.writer(file)
    data.writerow(['5','karthik','pfs'])
    data.writerow(['6','keerthi','pfs'])   



import csv

with open ('product.csv','a',newline='') as file :
    data=csv.writer(file)
    data.writerow(['product_ids','product','price']) 
    data.writerow(['1','phone','20000'])
    data.writerow(['2','laptop','60000'])   
    data.writerow(['3','mouse','4000'])
    data.writerow(['4','charger','6000']) 



import csv

with open ('product.csv','r',newline='') as file :
    data=csv.reader(file)
    for i in data:
        print(i)




import json

with open ('demo.json','w') as file :
    data=[
        {'id':'1','name':'karthi'},
        {'id':'2','name':'keerthi'},
        {'id':'3','name':'dileep'},
        {'id':'4','name':'akshay'},
        ]
    json.dump(data,file,indent=4)
    print("data saved sucessfully!")

    
import json
with open ('demo.json','r') as file :
    data=json.load(file)
    for i in data:
        print(i)


'''
import json
#read
with open ('demo.json','r') as file :
    data=json.load(file)
data.append({'id':'6','name':'varsha'})
with open ('demo.json','w') as file :
    json.dump(data,file,indent=4)

























