#Program to Get the Class Name of an Instance
# using __.__name__
class Smartphone():
    def name(self,name):
        return name
s1=Smartphone()
print(s1.__class__.__name__)