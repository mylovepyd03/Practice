class Book():
    #attribute, property 
     title=None
     ISBN=None
     pages=None 
     year=-1
     price=-2

     #method
     def settitle(self,newTitle):
         self.title=newTitle
     def getTilte():
         return self.title   
        
b=Book()
print(b.title)

b.setTitle('이기적 유전자')
print(b.title)
print(b.getTitle())
