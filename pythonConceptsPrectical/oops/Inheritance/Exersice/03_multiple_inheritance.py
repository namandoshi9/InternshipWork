# Create three classes A, B, and C. 
# Class A has a method method_A that returns "Method A from class A," class B has a method method_B that returns "Method B from class B," and class C inherits from both A and B.
# Create an instance of C and print the output of its methods.

class A:
    def method_A(self):
        return "Method A from class A"

class B:
    def method_B(self):
        return "Method B from class B"

class C(A,B):
    def method_C(self):
        return "Method C from class A and B Both"

c1 = C()
print(c1.method_A())
print(c1.method_B())
print(c1.method_C())

