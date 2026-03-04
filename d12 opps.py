'''
class flipkart:
    discount=10
    
    @classmethod
    
    def updateddiscount (cls,newdiscount):
        cls.discount=newdiscount
    def userinfo(self,name,phonenumber):
        self .name = name
        self.phonenumber=phonenumber
        print(f'username:{self.name}')
        print(f'phone number:{self.phonenumber}')
    @staticmethod
    def banner():
        print("welcome to the flipkart\n10%discount is going on ,shop now")
            
        
varsha=flipkart()
varsha.userinfo('varsha',9876543210)
varsha.updateddiscount(30)
flipkart.updateddiscount(40)
varsha.banner()
flipkart.banner()

anvika=flipkart()
anvika.userinfo('anvika',9876543210)
anvika.updateddiscount(30)
flipkart.updateddiscount(40)
anvika.banner()
flipkart.banner()

bhavana=flipkart()
bhavana.userinfo('bhavana',9876543210)
bhavana.updateddiscount(30)
flipkart.updateddiscount(40)
bhavana.banner()
flipkart.banner()

class instgram :
    def __init__(self,username,password):
        self.username = username
        self.password=password
        print(f"hey {self.username},welcome to the instgram!!!")
anvika= instgram('anvika','a@123')
varsha=instgram('varsha','v@123')






#another program (instgram)

class instgramv1:
    def __init__(self,username):
         self.username = username
         print(f"hey{self.username},welcome to the instgram!!!")
    def reels(self):
        print("you can upload and scroll the reels")
    def posts(self):
        print("you can post your pics")
class instgramv2(instgramv1):
    def __init__(self,username):
         super().__init__ (username)
    def story(self):
        print("you can upload the story")

class instgramv3(instgramv2):
    def __init__(self,username):
         super().__init__ (username)
    def note(self):
        print("you can upload a note")
  
class instgramv4(instgramv3):
    def __init__(self,username):
         super().__init__ (username)
    def live(self):
        print("you can have a live ")

class creator(instgramv4):
    def __init__(self,username):
         super().__init__ (username)
    def insights(self):
        print("you can check you post insights")
class business(instgramv4):
    def __init__(self,username):
         super().__init__ (username)
    def insights(self):
        print("you can contact them mail and number ") 
anvika = instgramv1('anvika')
anvika.reels()
anvika.posts()

varsha = instgramv2('varsha')
varsha.reels()
varsha.posts()
varsha.story()

sirisha = instgramv3('sirisha')
sirisha.reels()
sirisha.posts()
sirisha.story()
sirisha.note()

bhavana = instgramv4('bhavana')
bhavana.reels()
bhavana.posts()
bhavana.story()
bhavana.note()
bhavana.live()


'''


#hotstar program

class hotstar:
  def __init__(self,username):
      print(f"hey{self.username},welcome to the hotstar!!!")
  def playvideo(self):
      print("ads will run  ") 
      print("no download option  ") 
         






























































    
