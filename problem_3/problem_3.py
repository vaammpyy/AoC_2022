import numpy as np

f=open("problem_3.txt",'r')
lines=f.readlines()

s=0

def score(c):
    if ord(c)>91:
        return(ord(c)-96)
    else:
        return(ord(c)-64+26)

for i in range(len(lines)):
    t=0
    string=lines[i]
    N=len(string)-1
    for i in range(0,int(N/2)):
        c=string[i]
        for j in range(int(N/2),N):
            if string[j]==c:
                s+=score(c)
                t=1
                break
        if t==1:
            break
print("Sum of priorities is {}!".format(s))

badges=[]
print(len(lines))

pri=0

for i in range(0,len(lines),3):
    str_1=lines[i]
    str_2=lines[i+1]
    str_3=lines[i+2]
    strg=[str_1,str_2,str_3]
    str_0=str_1+str_2+str_3
    char=list(str_0)
    for i in range(len(char)):
        c=char[i]
        if c in list(str_1):
            if c in list(str_2):
                if c in list(str_3):
                    badges.append(c)
                    pri+=score(c)
                    break

print(pri)
print(badges)


            
            
        








