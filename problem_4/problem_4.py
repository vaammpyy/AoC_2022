f=open("problem_4.txt",'r')
lines=f.readlines()

bound=[]
num=''

for i in range(len(lines)):
    stri=lines[i]
    for i in range(len(stri)):
        if stri[i]=='-' or stri[i]==',' or stri[i]=='\n':
            bound.append(num)
            num=''
            continue
        else:
            num+=stri[i]

c=0

for i in range(0,len(bound),4):
    if int(bound[i])<=int(bound[i+2]) and int(bound[i+1])>=int(bound[i+3]):
        c+=1
    elif int(bound[i+2])<=int(bound[i]) and int(bound[i+3])>=int(bound[i+1]):
        c+=1
    else:
        continue
print("Number of pair for which the interval contains the other is {}".format(c))

c=0

for i in range(0,len(bound),4):
    if int(bound[i+1])>=int(bound[i+2]) and int(bound[i])<=int(bound[i+3]):
        c+=1
    else:
        continue
print("Number of overlapping pair for which the interval contains the other is {}".format(c))
