# import os
# if (not os.path.exists("data")):
#  os.mkdir("data")
# for i in range(0,100):
#     # os.rename(f"data\date{i+1}",f"data/tutorial{i+1}")
#     os.mkdir(f"data/date{i+1}")
    
    
# f=open('myfile.txt','r')   
# text=f.read()
# print(text)


# 


# class Book():
#     def __init__(self,title, author, pages):
#      self.title=title
#      self.author=author
#      self.pages=pages
#     def is_big_book(self):
        
#     #  print(f"THE NAME OF THIS BOOK IS{self.title},AND THE AUTHOR IS {self.author}, IT IS OVER {self.pages} PAGES ")
#      if self.pages>300:
#         return True
#      else :
#         return False
# book1=Book("GOBLET OF FIRE","J.K ROWLING",400)   
# book2=Book("DAY IN MUSSORI","RUSKIN BOND",200)  

# print(book1.is_big_book()) 
# print(book2.is_big_book())    



# def my_decorator(func):
#     def wrapper():
#      print("staring...")   
#      func()
#      print("done!")    
#     return wrapper


# @my_decorator
# def name():
#     print("ANIRUDH")     
# name()      

# def my_decorator(func):
#     def wrapper():
#      print("")
#      func()
#      print()
#     return wrapper

# @my_decorator
# def time():
#     print("")
# time()    


# class calculator():
#     @staticmethod
#     def solve(a,b):
#         return a+b ,a-b,a/b,a*b
    
# print(calculator.solve(2,3))    


# class StringUtlis():
#      @staticmethod
#      def is_palindrome(string):
#          return string==string[::-1]
     
# print(StringUtlis.is_palindrome("mom"))     

class car():
    car_wheel=4
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
       
        
    def callin(self)    :
        print(f"its {self.model} and it belong to the brand {self.brand} it is equipped with {self.car_wheel} wheels ")
        
        
c1=car("2022 XRZ","MASSARATI")    
c1.callin()
# print(f"comes with {c1.car_wheel}")
c2=car("2025 R400","NIMSUM")    
c2.callin() 
# print(f"comes with {c2.car_wheel} wheels")

print(dir(c1))      # shows all attributes and methods
print(c1.__dict__)  # shows instance variables only
help(car)          