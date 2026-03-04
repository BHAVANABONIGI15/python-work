'''
file=open('sample.txt','r')

content1=file.read()
file.seek(0)
content2 =file.readline()
file.seek(0)
content3 = file.readlines()
print(content1,content2,content3,sep='\n\n')
file.close()












file=open('sample.txt','w')
file .write("hello anvika ")
file.close()






file=open('sample.txt','a')
file .write(" welcome to the python class  ")
file.close()







file=open('sample.txt','a+')
file .write(" \n file operations  ")
file.close()






file=open('sample.txt','r+')
file .write(" \n file operations  ")
file.seek(0)
print(file.read())
file.close()



with open('sample.txt','r+')as file:
    file .write(" \n file operations  ")
    file.seek(0)
    print(file.read())
  





import csv
with open('excel.csv','r')as file:
     content = csv.reader(file)
     for row in content:
         print(row)







import csv
with open('excel.csv','r')as file:
     content = csv.reader(file)
     for row in content:
         print(row[2])

'''

               







l=[1,2,3,3,4,0,0,0,5,6,6,7,7,0,0,0,0]

while 0 in l :
        l.remove(0)
print(l)






















