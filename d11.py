
'''
try:
    a={1:1,2:4,3:9}
    
    print(a[4])
except NameError:
    print('a is not defined')
except ValueError :
    print("enter the requested data type")
except TypeError :
    print("Data types are different.")
except ZeroDivisionError :
    print("can't divide with zero")
except IndexError:
    print("The index is not prsent")
except KeyError:
    print("In dict this key is not present")

else:
    print('no errors')
finally:
    print("end of the block")



try:
    a=a+'8'
    print(a[4])
except(NameError,ValueError,TypeError,ZeroDivisionError,IndexError,KeyError )as e :
       print(f'error occoured:{e}')
else:
    print('no errors')
finally:
    print("end of the block")
    
'''
try:
    a=int(input())
    if a<0:
        raise Exception ("enter the postive value")
except Exception as e:
    print(f'error occured :{e}')
else:
    print('no errors')
finally:
    print("end of the block")









































    
