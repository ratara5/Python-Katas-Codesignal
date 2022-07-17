from argparse import ArgumentDefaultsHelpFormatter
from email.errors import StartBoundaryNotFoundDefect
from fnmatch import translate
import itertools
import re
from tarfile import USTAR_FORMAT
from urllib.request import AbstractDigestAuthHandler
from xml.etree.ElementTree import Comment
from xmlrpc.client import SERVER_ERROR

from numpy import right_shift
from pandas import Series


a=[1,2,3,4,5,1,2]
list=a[:]
c,d,*list=list
print(list)

# isAdmisibleOverpayment
# Arcade 
# Practice your coding skills while unlocking the arcade map
# the arcade map 
# Company challenges
# Solve interesting  
# Interview Practice
# Prepare for technical interviews using real interview question from top companies
# Select a study plan to get Started 

# Putting neglected tropical diseases on the global health agenda 

# Latest news and comment 

# A new vision for death and dying

# Rebecca Lee Crumpler: first Black woman physician in the USA 

# Archbishop Desmond Tutu and the universality of the health and human rights 

# Managing Diabetes and Homelessness 


# Summary 
# Meliodiosis is a tropical infection caused by the soil bacterium Burkholderia pseudomallei. Despite the substantial impact of this often overlooked pathogen on the both the health-income countries around the world, meliodosis is not oficially classsfield as a neglected tropical disease (NTD) by WHO. Meliodiosis causes a higher estimated disease burden and mortality than many other recognised NTDs, whit deaths primarily ocurring among rural poor populations in low-income and middle-income countries. Fortunately,the impact of meliodosis as an NTD. We urge member states to requesst that WHO revisit their NTD list appeal to government and philanthropid roganisations to establish programmes in endemic countries to control meliodosis in order to reduce its global health burden

# This article can be found in the following collections:
# Global Health 
# Infectious Diseases 
# Neglected tropical diseases
# Emerging infectious diseases


# Global,regional, and national sex differences in the global burden of tuberculosis by HIV status, 1990-2019: results from the Global Burden of Disease Study 2019.StartBoundaryNotFoundDefect

# Risk factors for the streap of vaccine-derived type 2 polioviruses after global withdrawal of trivalent oral poliovirus vaccine and the effects of outbreak responses with monovalent vaccine: a retrospective analysis of surveillance data for 51 countries in Africa 

# Complications and mortality of non typhoidal salmonella invasive disease: a global systematic review and meta-analysis 

# Persistence of protection against SARS-CoV-2 clinical outcomes up to 9 months since vaccine completion: s retrospective observational analysis in Lombardy, Italy 

# Safety and immunogenicity of an AS03-adjuvanted SARS-CoV-2 recombinant protein vaccine (CoV2 preS dTM) in healthy adults: interim findings from a phase 2, randomised, dose-finding, multicentre study

# Combining baloxavir marboxil with standard-of-care nuraminidase inhibitor in patients hospitalise with SERVER_ERRORinfluenza (FLAGSTONE): a randomised, paralell-group, double-blind, placebo-controlled, superiority trial

# Sepsis: a roadmap for future research
# Vaccination and haematological malignancies
# Combating Childhood infectionts in LMiCs: evaluating the contribution of Big Data

# Sexually transmitted infections: challenges ahead

# Fluid therapy for severe malaria

# A call to action: time to recongnise melioidosis are a neglected tropical disease

# Explore all global health and clinical Series
# Read all global health and clinical Commissions

# Prof Beaze Kampmann, Dr Karen Keddy, and Prof Peter Ghazal
# discuss a new cross-journal Series in the Lancet Infectious 
# Diseases and EBioMEdicine addressing the potential for and challenge of applying big data to childhood infectious diseases in LMICS

# A new Article in the Lancet Infectious Diseases highlights how changing immunity profiles motivate the need for better responses to outbreaks of polio in Africa

# Paul Chapman and colleagues pressents the results of an innovative trial assesign the safety of vaccinating healthy volunteers with attenuated Necator americanus hooknown larvae

# To invert string
p="palabrerias"
print(p[::-1])

# ASCII of char
print(ord('a'))

# Encrypting key 
key='zwyxwvut'
table={ord('a')+i:ord(k) for i, k in enumerate(key)}
password='cadaca'
print(password.translate(table))

#
import re 
s="We expect the %f%%"
s=re.sub('%%','{nothing}',s)
s=re.sub('%[bcdefgxXvC]','{}',s)
s=re.sub('{nothing}','%',s)

#
commit='?shkjh0'
''.join(char for char in commit if char not in ['+','0','!','?'])

#students
s=[1,5,11,6,8,9,7]
print(sum(s[::2])-sum(s[1::2]))

#delete toDo
def remove_tasks(k,t):
    del t[::k]
k=2
t=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
remove_tasks(k,t)
print(t)

#
print('esta es la lista t: '+str(t))
print('esta es la lista t: {}'.format(t))

#
n=20
ch=':-)'
#print(n*ch)
repeat_chars=lambda ch,n:n*ch

#
answer=[True, True, False, True] #answer list student in test
p=2 #penalty for wrong answer

res=0 #initialize result
qP=lambda i,ans:i+1 if ans==True else -p
for i, ans in enumerate(answer):
    res+=qP(i,ans)

print ("The points in the exam are {}".format(res))

#
persons=["Lucas Tañeda","Camila Nesa","Jhony Melavo","Paco Rido","Pepe Lota"]
persons.sort(key=lambda n:n.split()[-1])
print(persons)

#
ids_list=[529665,909767,644200]
k=3

digit_sum=lambda id:sum(int(x) for x in str(id))
ids_sum=0 
for qid in ids_list:
    ids_sum+=digit_sum(qid)
print(ids_sum%k==0)

#Spiral matrix 30 (to do)

#Construct shell 31

#Word Powder 32

#Cool Pairs 33 (todo)

# Multiplication Table 34

# 
import functools

list=[1,2,4,8,3,7,2,1]
print(max(list))
prod=functools.reduce(lambda x,y: x*y, list)
print(prod)
print()


# For one list a, the list b will be (per index): zero equals, b_one equal a_last, b_two equal a_one, b_three equal a_secondLast and so on
def solution(a):
    b=a[:]
    if len(a)<=2:
        return b
    else:
        b[0]=a[0] 
        b[1]=a[-1]
        b[2]=a[1]
        b[3::]=a[::-1][1:-2:] #el índice negativo de la lista pasa a ser positivo y se le resta 1 a su valor absoluto para la lista invertida, lo mismo sucede con los índices positivos 
        return b

print(solution([1,2,3,4,5,6]))
#if a=[1,2,3,4,5,6] b=[1,6,2,5,4,3]
#if a=[1,2,3,4,5,6,7,8], b=[1,8,2,7,6,5,4,3]

#form row of blocks (left to right, up to down) wich sum is minimum, for a height
blocks=[3,3,2,1,5,4]
h=2
#the above values should return row1=3,3,2,1 row2=5,4 // sum(row1)=9, sum(row2)=9
blocks=[5,5,9,2,3,4,10]

#if h=2, the major list for a subllist is 7-1=6
#if h=3, the major list for a subllist is -1=6

for i,k in range(0,len(blocks)):
    print("the sum blocks between 0 and "+str(i)+" (inclusive) is: "+str(sum(blocks[:i+1])))
    print("the sum blocks between "+str(i+1)+" (inclusive) and "+str(k)+" is: "+str(sum(blocks[i+1:k])))
    print("**********************************")

#
from itertools import combinations
def gen_sublists(lista):
    sublists=[]
    for i in range(0,len(lista)+1):
        sublist=[list(c) for c in combinations(lista,i)]
        if len(sublist)>0:
            sublists.extend(sublist)

    return sublists

print(gen_sublists(['p','q','r','s','t']))

#probar con islice y con accumulate
statues=[0, 2]
list=[n for n in range(10) if n not in statues]
print (list) 

#
def solution(sequence): 
    for i in range(0,len(sequence)):
        c=sequence[:i]+sequence[i+1:]   
        if all(x<y for x, y in zip(c, c[1:])):
    #         return True
    # return False  

sequence=[1,3,2]
minimun=1
maximum=3
c_s=[1,3,2]
print()

n=29
n[0]+n[1]

s=[1,2,3,4,5]
a='asb'
a_s=a.split()
b='svbasbbsbc'
b_s=b.split()
[True if a_s in b_s].count(True)
print(a in b)

import itertools
p=[[0,11],[-7,1],[-5,-3]]

dist=[]
for c in itertools.combinations(p,2):
    pair=list(c)
    print(pair)

sequence="[][{](})"
for i in range(0,len(sequence)-1):
    if sequence!="" and (sequence[i]=='{' and sequence[i+1]=='}') or (sequence[i]=='[' and sequence[i+1]==']') or (sequence[i]=='(' and sequence[i+1]==')'):
        print(True)

#
seq=[1,2,3,4,5]
f=lambda i, lista: lista[:i]+lista[i+1:]
for i in range(0,len(seq)):
    c=f(i,seq)

    print(c)

#
def solution(value1, weight1, value2, weight2, maxW):
    max_val=0
    if weight1+weight2<=maxW:
        return value1+value2
    else:
        if weight1<=maxW and weight2<=maxW:
            max_val=max(value1,value2)
        elif weight1<=maxW:
            max_val=value1
        elif weight2<=maxW:
            max_val=value2
    return max_val
 
#
def solution(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    else:
        return max(value1 if weight1 <= maxW else 0, value2 if weight2 <= maxW else 0)


n=902200100

for i in range(0, len(str(n))):
        if n%10==0:
         n/=10
         i
print(n)
if '0' in str(n):
    return True
return False

n=15
sn=list(str(n)[::-1])
print(sn)
for i in range (0,len(sn)-1):
    if int(sn[i])>=5:
        sn[i+1]=str(int(sn[i+1])+1)
    sn[i]='0'
int(''.join(sn[::-1]))

import math
n=400
for a in range(0,12):
        for b in range(2,12):
            if math.pow(a,b)==float(n):
                print(True)
                break
print(False)

import math
print(type(math.pow(5,3)))

import math
def solution(n):
    for a in range(0,math.sqrt(n)+1):
        for b in range(2,12):
            if math.pow(a,b)==float(n):
                return True
    return False
solution(125)


def solution(a0):
    ak=0
    count=1
    ak_1=a0
    while ak!=a0:
        ak=sum(int(x)**2 for x in str(ak_1))
        ak_1=ak
        count+=1
    return count

print(solution(103))

print(type(sum(int(x)**2 for x in str(10))))

def solution(current, numberOfDigits):
    while numberOfDigits>=len(str(current+1)): 
        numberOfDigits-=len(str(current))
        current+=1
    return current

print(solution(1,5))

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


def solution(n):
    def count_div(num):
        return len(list(filter(lambda i: num%i==0, range(1,num//2+1))))+1

    m=list(map(lambda i: count_div(i),range(1,n+1)))

    z=dict(zip(range(1,n+1),m))

    return(z)

    
        

def solution(n):
    d = [sum(i%j==0 for j in range(1,i+1)) for i in range(1,n+1)]
    w = [sum(j>m for j in d[:i]) for i,m in enumerate(d)]
    return [max(w),w.count(max(w))]




