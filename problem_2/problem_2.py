f=open("problem_2.txt",'r')
lines=f.readlines()

result_strat_1=["B X\n","C Y\n","A Z\n","A X\n","B Y\n","C Z\n","C X\n","A Y\n","B Z\n"]
result_strat_2=["B X\n","C X\n","A X\n","A Y\n","B Y\n","C Y\n","C Z\n","A Z\n","B Z\n"]


s_1=0
s_2=0
for i in range(len(lines)):
    s_1+=result_strat_1.index(lines[i])+1
    s_2+=result_strat_2.index(lines[i])+1

print("Total score is {} with strategy 1".format(s_1))
print("Total score is {} with strategy 2".format(s_2))
