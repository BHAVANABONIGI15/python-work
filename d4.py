'''
pwd = input("enter the password: ")

if len(pwd)>=8:
    s=set()
    for i in pwd:
       if i .isupper():
          s.add("upper")
       elif i .islower():
          s.add("lower")
       elif i.isdigit():
          s.add("digit")
       else:
          s.add("splchar")
    if len(s)==4:
        print("strong password")
    else:
        print("weak password.password needs to have upper,lower,digit,splchar")
        
else:
    print("length needs to be >=8")

name = input("enter the name: ")
dob=input("enter the dob [yyyy-mm-dd]:")
username= name[:2]+name[-2:]+dob[-2:]+dob[2:4]
print(f"hi {name}!\nyour username:{username}")
'''          
data={
1: { 'product':'rice','price':60},
2: { 'product':'milk','price':30},
3: { 'product':'sugar','price':20},
4: { 'product':'salt','price':10},
5: { 'product':'choclate','price':40},
6: { 'product':'egg','price':6},
7: { 'product':'oil','price':160},
8: { 'product':'soap','price':45},
9: { 'product':'paste','price':70},
10:{ 'product':'jam','price':50},

}




print('Index'.ljust(7,' '),'Product Name'.ljust(20,' '),'Price'.ljust(10,' '))
for i in data:
    print(str(i).ljust(7,' '),data[i]['product'].ljust(20,' '),str(data[i]['price']).ljust(10,' '))



indexes = list(map(int,input("Enter the indexes: ").split()))


print("Bill".center(30,'-'))
total_bill=0
for i in indexes:
    print(f'{data[i]["product"]}- {data[i]['price']*{indexes.count(i)}={data[i]['price']*indexes.count(i)}''')total_bill+= data[i]['price']*indexes.count(i)))
    total_bill+= data[i]["price"]

print(f"Your Bill: {total_bill}")
    
