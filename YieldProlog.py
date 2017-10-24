
class Var:
    def __init__(self,val=None):
        self.val = val
        if val: self.bound = True
        else: self.bound = False
    def __repr__(self): return '<%s>' % self.val
    def __lshift__(self, arg): # unify
        if not self.bound:
            if isinstance(arg, Var):
                self.val = arg.val
            else:
                self.val = arg
            self.bound = True
            yield self
            self.bound = False  # drop binding
        elif isinstance(arg, Var) and self.val == arg.val:
            yield self
        elif self.val == arg:
            yield self

for i in Var(1) << 1: print i            
for i in Var(2) << Var(2): print i            

def getval(val):
    if isinstance(val,Var) and val.bound: return val.val
    return val

def unify(arg1,arg2):
    val1,val2 = getval([arg1,arg2])
    if isinstance(val1, Var):
        for i in val1 << val2:
            yield i
    elif isinstance(val2,Var):
        for j in val2 << val1:
            yield j
    else:
        # arguments are normal types with equal values 
        if val1 == val2:
            yield val1

def woman(P):
    for i in unify(P,'mia'): yield i
    for i in unify(P,'jody'): yield i
    for i in unify(P,'yolanda'): yield i
    
def brother(Person,Brother):
    for i in unify(Person,'mia'):
        for j in unify(Brother, 'tony'):
            yield (i,j)
    for x in Person << 'jody':
        for y in Brother << 'bill':
            yield (x,y)
    
def playsGuitar(P):
    P.val = 'jody' ; yield P

for i in woman('mia'): print 'mia = ',i
for i in woman('jody'): print 'mia = ',i
W=Var() ; B=Var()
for i in woman(W):
    for j in brother(W, B):
        print 'woman', W, 'has brother', B
for i in brother(Var(),Var()): print 'brother',i
