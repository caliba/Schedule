class A:

    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = "sb"


dic = {1:A(),2:A()}

print(dic.values())