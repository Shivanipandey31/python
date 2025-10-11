# class Person:
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age
# class Faculty(Person):
#     def _init_(self, name, age, faculty_id):
#         super()._init_(name, age)
#         self.faculty_id = faculty_id
#         self.publications = []

from abc import ABC
class Car(ABC):
    def _init_(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    @abstractmethod
    def print_details(self):
        pass
class matchback(Car):
    def print_details(self):
        print("Brand",self.brand)
        print("Model",self.model)
        print("Year",self.year)
    def sunroof(self):
        print("Not having this features")
c1=matchback()