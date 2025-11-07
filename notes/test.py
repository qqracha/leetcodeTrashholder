class Rogen:
    def __secret(self):
        return "hackme1337"

    def registr(self):
        login = "Egor\n" + self.__secret()
        return login
    
r = Rogen()
print(r.registr())
try: 
    print(r.__secret())
except AttributeError:
    print('HERE IS NOTHING!!!')
# class Map: 
#     def __init__(self): 
#         self.__geek() 
        
#     def geek(self): 
#         print("In parent class") 
  
#     # private copy of original geek() method 
#     __geek = geek    
  
# class MapSubclass(Map): 
      
#     # provides new signature for geek() but 
#     # does not break __init__() 
#     def geek(self):         
#         print("In Child class")
        
# # Driver's code
# obj = MapSubclass()
# obj.geek()