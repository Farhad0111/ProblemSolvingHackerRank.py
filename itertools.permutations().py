from itertools import permutations
class Farhad:
    def __init__(self):
        self.a,self.n =input().split()
    def faru(self):
        self.p=sorted(permutations(self.a,int(self.n)))
        for j in list(self.p):
            print(*j,sep='')
farhad=Farhad()
farhad.faru()