#w.a.p.p create a class bike and given two attribute name and gear and access with bike1 object

class Bike:
    name = ""
    gear = 0
    
bike1 = Bike()

bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"name : {bike1.name}, Gears : {bike1.gear}")