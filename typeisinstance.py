class smartphone:
    def name(self):
        pass
class nokia(smartphone):
    def phone_name(self):
        pass
obj_s=smartphone()
obj_n=nokia()
print("for type()function")
print(type(obj_s)==smartphone)
print(type(obj_n)==nokia)
print("for isinstance()function")
print(isinstance(obj_s,smartphone))
print(isinstance(obj_n,smartphone))
