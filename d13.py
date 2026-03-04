'''

class snapchat:
    def __init__(self,username,password,friends ):
        self.username = username
        self.__password = password #private
        self._friends = friends #protected
    def getpassword(self):
        return self.__password
    def setpassword(self,new_password):
        self.__password = new_password
    @property
    def oprfriends(self):
        return self._friends
    @oprfriends.setter
    def oprfriends(self,newfriend):
        self._friends.append(newfriend)
anvika = snapchat ('anvika','123',['keerthi','karthi'])
print(f'Name before modification:{anvika.username}')
anvika.username = 'anvi'
print(f'Name after modification: {anvika.username}')

print(f'password before modification:{anvika.getpassword()}')
anvika.setpassword('143')
print(f'password after modification:{anvika.getpassword()}')

print(f'friends before modification: {anvika.oprfriends}')
anvika.oprfriends = 'chintu'
print(f'friends after modification: {anvika.oprfriends}')

'''


from abc import ABC,abstractmethod  #ABC=Abstract Base Class
class BankAccount(ABC):
    def checkbalance(self):
        print("you can checkout your balance")
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class SavingAccount(BankAccount):
    def deposit(self):
        print("2 lakhs per day")
    def withdraw(self):
        print("1 lakh you can withdraw")
        
class CurrentAccount(BankAccount):
    def deposit(self):
        print("unlimited deposit")
    def withdraw(self):
        print("unlimited withdraw")
        
class JointAccount(BankAccount):
    def deposit(self):
        print("only those 2 people can deposit")
    def withdraw(self):
        print("1-2 lakhs per day you can withdraw")
        
class SalaryAccount(BankAccount):
    def deposit(self):
        print("no limit")
    def withdraw(self):
        print("20K-1L per day")
        
class PensionAccount(BankAccount):
    def deposit(self):
        print("no deposit")
    def withdraw(self):
        print("40K per day")
        
print("---abhinandhan---")
abhinandhan= SavingAccount()
abhinandhan.checkbalance()
abhinandhan.deposit()
abhinandhan.withdraw()

print("---praveen---")
praveen=CurrentAccount()
praveen.checkbalance()
praveen.deposit()
praveen.withdraw()

print("---saaketh_nikhil---")
saaketh_nikhil=JointAccount()
saaketh_nikhil.checkbalance()
saaketh_nikhil.deposit()
saaketh_nikhil.withdraw()

print("---shanmukh---")
shanmukh=SalaryAccount()
shanmukh.checkbalance()
shanmukh.deposit()
shanmukh.withdraw()

print("---swapnil---")
swapnil=PensionAccount()
swapnil.checkbalance()
swapnil.deposit()
swapnil.withdraw()
