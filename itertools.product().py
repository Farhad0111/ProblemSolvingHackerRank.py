import itertools
class Farhad:
    def __init__(self):
        self.l1=list(map(int,input().split()))
        self.l2=list(map(int,input().split()))
    def faru(self):
        print(*itertools.product(self.l1,self.l2))
farhad=Farhad()
farhad.faru()