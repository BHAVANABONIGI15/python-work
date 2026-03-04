
'''
def student_data(info):
    print(f'name: {info[0]}')
    print(f'course: {info[1]}')
    print(f'grs_year: {info[2]}')
    print('-----end----')

data = [['varsha','pfs','2026'],
        ['sirisha','dsa','2026'],
        ['karthik','jfs','2026'],
        ['anvika','pfs','2026'],
        ]
for i in data:
    student_data(i)
    


#functional arugements  ....
  
    


def display (uname,email,password):
    print(f'username: {uname}')
    print(f'email : {email}')
    print(f'password : {password}')
    print('\n\n')
display('anvika','anvika@gmail.com','anvika@15')
display('anvika@15','anvika','anvika@gmail.com')

display('anvika@gmail.com','anvika@15','anvika')



def display (uname,email,password,status='absent'):
    print(f'username: {uname}')
    print(f'email : {email}')
    print(f'password : {password}')
    print(f'status : {status}')
    
    print('\n\n')
display('anvika','anvika@gmail.com','anvika@15','present')  
'''
def display(*names):
    for i in names:
        print(i)
    else:
        print("------------end of the list ----------")
display('varsha')
display('anvika','krishna','radha')
display('karthik','dileep')
