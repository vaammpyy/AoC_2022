f=open("problem_5.txt",'r')
#lines=f.readlines()
#text=f.read().split(' ')
text=f.readlines()

stack=[]
moves=[]

sep=text.index('\n')

for i in range(len(text)):
    if i==sep:
        continue
    elif i<sep:
        stack.append(text[i])
    elif i>sep:
        moves.append(text[i])
    else:
        continue
arr_st=[]

for j in range(len(stack)):
    buff_arr=[]
    for i in range(0,len(stack[1]),4):
        stri=stack[j]
        buff_arr.append([stri[i:i+3]])
    arr_st.append(buff_arr)
        
#print(arr_st[0][1])

moves_arr=[]

for j in range(len(moves)):
    buff_arr=[]
    t=0
    stri=moves[j]
    str_t=[]
    for i in range(len(stri)):
        if stri[i]==' ' or stri[i]=='\n':
            t=not t
            continue
        if t==1:
            str_t.append(int(stri[i]))
        if stri[i]==' ' or stri[i]=='\n':
            t=not t
            continue
    moves_arr.append(str_t)



print(moves)
print(moves_arr)

