
# # Defining Clases
# class Person:
#     name = "Emre"
#     age = 32
    
# person1 = Person()
# person2 = Person()

# print(person1.name)
# print(person2.name)

# #Obje icerisinde sonradan bir degisken olusturabiliyoruz!
# Person.job = "Teacher"
# print(person1.job)

# #Class attrubutes ve instance attributes
# Person.name = "Hatice"
# person1.name= "Ela"
# person1.age = 2
# print(person1.name,person1.age)
# print(person2.name,person2.age)


#Self Keyword

# class Person:
#     name = "Emre"
#     age = 32

#     def test(self): # burdaki self js deki this yerini tutuyor.
#         print(':>>>>:Metodun ciktisi')
    
#     def get_details(self):
#         print('name:',self.name,'age:',self.age,'location',self.location)#sadece name yazarsak attributelerre ulasamiyor. self.name yazmamiz gerekiyor


#     def set_details(self,name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location # instance(person1 ) icerisinde self.location diyerek locationu tanimliyoruz. Cünku location digerleri gibi class icerisinde tanimlanmadi.


# person1 = Person()

# person1.test()
# Person.test(person1)
# person1.set_details('Ege',1,'Adana')
# person1.get_details()



#--------------
# class Person:
#     name = "Emre"
#     age = 32

#     def get_details(self):
#         print('name:',self.name,'age:',self.age,'location',self.location)


#     def set_details(self,name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location 
        
#         @staticmethod #instancelarla hicbir alakasi yok, instance attributelere ulasilamiyor statik metodlarla
#         def salute():
#             print('Hi there',Person.name)

# Person.salute()
# person1= Person()
# person1.set_details('Rafe',39,'Ankara')
# person1.salute()


#Special Methods
# class Person:
#     company = 'Clarusway'

#     def __init__(self, name, age):#__init__ Person classindan bir instance olusturursam init icerisinde tanimli seyler alt class a otomatik tanimlanir.
#         self.name = name
#         self.age = age
        
#     def __str__(self):
#             return f"Name: {self.name}  Age:{self.age}"

#     def __len__(self):
#             return self.age

# person1= Person('Berry',44) 
# # print(person1.name,person1.age)

# lst =[1,2,3]
# print(len(lst))
# print(len(person1))
# print(person1) #Person icerisinde str diye bir metod arar ve onu yazdirir yoksa Personun obje oldugunu söyleyen mesaj döndürür
# print(person1.__len__())

#>>>>>>>>>>>>>>>>>Abstraction and encapsulation<<<<<<<<<<<<<<<<<

#encapsulation verilerin disa kapanmasi icin güvenlik iciin
#Abstraction istenmeyen ayrintilari gizleme demektir.

# lst = [3,2,5,9,1]
# lst.sort()
# print(lst)

# class Person:
#     company = 'Clarusway'
#     def __init__(self,name,age):
#         self.name= name
#         self.age = age
#         self._id = 5000
#         self.__id1 =4000

# person1 =Person('Rafe',39)
# # person1.__id1 = 8000
# print(person1.__id1)
# person1._Person__id1 = 3000
# print(person1._Person__id1)


#>>>>>>INHERITANCE AND POLYMORPHISM
# class Person:
#     company = 'Clarusway'

#     def __init__(self,name,age):
#         self.name= name
#         self.age = age
     
#     def __str__(self):
#         return f"Name:{self.name} Age:{self.age} "

# class Lang:
#     def __init__(self,langs):
#         self.langs= langs


# class Employee(Person,Lang):
#     def __init__(self,name,age,path):
#         # self.name = name
#         # self.age = age
#         super().__init__(name,age,path)#kimden inherit edildiysen(türetildiysen) git onun initi ne göre islem yap
#         Lang.__init__(self,['Python','JS'])
#         self.path= path

# #Yukaridaki str yi yeniden düzenleyebilme de polymorphism oluyor.
#     def __str__(self):
#         return f"Name:{self.name} Age:{self.age} Path:{self.path}"
    
#     #Override
#     def details(self):
#         super().details()
#         print(f"Path: {self.path}")
#         print(f"Langs: {self.langs}")

# emp1 = Employee('Barry',44,'FS')
# # print(emp1)

# print(Employee.mro())#soy agacini cikariyor

# class Customer:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.__id = 1314
#         self.movements = []
#     def __str__(self):
#         return f"Name: {self.name} ID: {self.__id} "

#     def add_movement(self,amount,date,explain):
#         self.movements.append({'amount':amount,'date':date, 'explain':explain})
    
#     def all_movements(self):
#         for i in self.movements:
#             print(i['date'],i['amount'],i['explain'],)

#     def balance(self):
#         total = 0
#         for i in self.movements:
#             total += i['amount']
#         print('Total:',total)
#         # return sum(i['amount'] for i in self.movements)


# custom = Customer('Emre', 32)
# print(custom)
# custom.add_movement(5000,'13.10.2021','Salary')
# custom.add_movement(-1000,'14.10.2021','Rent')
# custom.add_movement(-500,'15.10.2021','Bills')
# custom.add_movement(-2000,'16.10.2021','C.Card')
# custom.all_movements()
# custom.balance()


class Dog:
    def walk(self):
        return "*walking*"
    def speak(self):
        return "Woof!"
class JackRussellTerrier(Dog):
    def talk(self):
        return super().speak()
bobo = JackRussellTerrier()
bobo.talk()
