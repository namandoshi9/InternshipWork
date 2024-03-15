from datetime import datetime

class Person:
    def __init__(self,name,country,bod):
        self.name = name
        self.country = country
        self.bod = bod
        
    def cal_age(self):
        today = datetime.now()
        bod = datetime.strptime(self.bod,"%y-%m-%d")
        age = today.year - bod.year - ((today.month,today.day) < (bod.month,bod.day))
        return age
    
if __name__ == "__main__":
    p_n = "naman"
    p_c = "India"
    p_bod = input("Enter  your birth date in format 'yy-mm-dd': ")
    
    person = Person(p_n,p_c,p_bod)
    
    age = person.cal_age()
    print(person.name,p_c,age)
    
        