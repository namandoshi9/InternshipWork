class A:
    def method_A(self):
        return "Method A from class A"
    
class B:
    def method_B(self):
        return "Method B from class B"
    
class C(A,B):
    def method_C(self):
        return "Method C from class C"
    
c1 = C()
print(c1.method_A())
print(c1.method_B())
print(c1.method_C())