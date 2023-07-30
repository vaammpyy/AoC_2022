#part 1
f=open('problem_1.txt','r')
lines=f.readlines()

N=len(lines)

a=0
elfs_cal=[]

brk=[0]

for i in range(N):
    if lines[i]=='\n':
        brk.append(i)
brk.append(N)

t=0

for i in range(1,len(brk)):
    s=0
    for j in range(brk[i-1]+t,brk[i]):
        
        s+=int(lines[j])
    t=1
    elfs_cal.append(s)

#print(elfs_cal)
mx=max(elfs_cal)


for i in range(len(elfs_cal)):
    if elfs_cal[i]==mx:
        print("Elf {} has {} clories which is the most calorie!".format(i+1,mx))

#part 2

elfs_sorted=sorted(elfs_cal,reverse=True)

print("Top 3 elfs have {} calories!".format(elfs_sorted[0]+elfs_sorted[1]+elfs_sorted[2]))
