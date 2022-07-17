def solution(l, r):   
    liss=[]
    for i in range(l,r+1):
        s_l=sum(int(x) for x in str(i))
        s_r=sum(int(x) for x in str(i))
        for n in range(i-s_l,i+s_r+1):
            if n in range(l,r+1) and i<n:
                t={i,n}
                if t not in liss:
                    liss.append(t)
    return len(liss)


l=12
r=108
liss=[]
for i in range(l,r+1):
    s=sum(int(x) for x in str(i))
    for n in range(i-s,i+s+1):
        if n in range(l,r+1) and i<n:
            t={i,n}
            if t not in liss:
                liss.append(t)
print(len(liss))

# returns the quantity of number's divisors
def count_div(num):
    return len([i for i in range(2,num//2+1) if num!=i and num%i==0])


#returns the weakness array for numbers since 1 to n
n=9
weakness_arr=[]
for i in range(1,n+1):
    weakness_i=0
    for j in range(1,i):
        if count_div(i)<count_div(j):
            weakness_i+=1
    weakness_arr.append(weakness_i)

weakest=max(weakness_arr)
result=[weakest,weakness_arr.count(weakest)]
print(result)

#returns module ot the even numbers between 2 and 10
a=list(map(lambda n:int(n/2),range(2,11,2)))
print((a))

#ver si números de 1 a n son divisores de 1 a n
n=9
for i in range(1,n+1):
    a=list((map(lambda x:x%i==0,range(1,n+1))))
    print((a))

#returns elements>5 in a tuple    
resultado = len(tuple(filter(lambda element: element>5, (1,2,3,4,6,8,9,40,10,11))))
print(resultado)

#generar lista de tuplas por combinación de tuplas dadas
l=10
r=12
[(a, b) for a in range(l, r+1) for b in range(l+2,r+5)]

def minor(d, dist):
    if d<min(dist):
        return d

def solution(a):
    dist=[9999]
    new=-1
    for i in range(0,len(a)):
        if a[i] in a[i+1:]:
            d=a[i+1:].index(a[i])+1
            if d<min(dist):
                new=a[i]
            dist.append(d)
    return new

solution([2,2])

def solution(a):
    s=[0]*len(a)
    for i in range(0,len(a)):
        if a[i]==s[i]:
            d=a[i+1:].index(a[i])+1
            if d<min(dist):
                new=a[i]
            dist.append(d)
    return new

solution([2,2])

print(set()=={})


def solution(s):
    for el in s:
        if el not in s[s.index(el)+1:]: 
            return el
    return '_'

s = "abacabad"
solution(s)


from distutils.errors import CCompilerError
from xmlrpc.server import list_public_methods
import numpy as np
def solution(a):
    return (np.transpose(a)).tolist()

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
solution(a)
print(len(a))

r=len(a)
c=len(a[0])
l=[]
for i in range(0,r):
    sl=[]
    for j in range(1,c+1):
        sl.append(a[c-j][i])
    print(sl)
    l.extend([sl])

print(l)



def existence(s):
    for el in s:
        if el not in s[s.index(el)+1:]: 
            return el
    return '_'


r=len(a)
c=len(a[0])
l=[]
for i in range(0,r):
    sl=[]
    for j in range(1,c+1):
        sl.append(a[c-j][i])
    l.extend([sl])


a=[[".","4",".",".",".",".",".",".","."], 
 [".",".","4",".",".",".",".",".","."], 
 [".",".",".","1",".",".","7",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".",".","3",".",".",".","6","."], 
 [".",".",".",".",".","6",".","9","."], 
 [".",".",".",".","1",".",".",".","."], 
 [".",".",".",".",".",".","2",".","."], 
 [".",".",".","8",".",".",".",".","."]]

#TODO:Generate submatrix 'list' of a with not repeated elements
#from itertools import permutations DOESN'T NEED BUT INTERESTING

pes=[[a,b] for a in range(0,3) for b in range(0,3)]
for p in pes:
    cc=[]
    for i in range(0+p[0]*3,3+p[0]*3):
        for j in range(0+p[1]*3,3+p[1]*3):
            if a[i][j]!='.':
                cc.append(a[i][j])
    print(cc)
    
#########SOLVABLE SUDOKU############
import numpy as np
def solution(a):
    #repeat
    def repeat(liss):
        print("I'm repeat")
        for elem in liss:
                if elem!='.' and elem in liss[liss.index(elem)+1:]:
                    return True

    #verify
    def verify(a):
        print("I'm in verify")
        for i in range(0,9):
                print(repeat(a[i]))
                if repeat(a[i])==True:
                    return False

    #verify by rows
    verify(a)
    print("I finished verify (out)")

    #transpose
    a_t_t=(np.transpose(a)).tolist()

    #verify by cols
    verify(a_t_t)

    #doesn't work
    def verify_submatrix(a):
        print("I'm in verify_submatrix")
        pes=[[a,b] for a in range(0,3) for b in range(0,3)]
        for p in pes:
            cc=[]
            for i in range(0+p[0]*3,3+p[0]*3):
                for j in range(0+p[1]*3,3+p[1]*3):
                    if a[i][j]!='.':
                        cc.append(a[i][j])
            if len(cc)>0 and repeat(cc)==False:
                return False

    if verify(a)==False or verify(a_t_t)==False or verify_submatrix==False:
        return False

    return True

solution(a)
############SOLVABLE SUDOKU###########