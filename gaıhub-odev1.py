import random as rand
ilksutun=[]
i=0
for i in range(3):
    a=rand.randint(0,100)
    ilksutun.append(a)
    i+=1
ikincisutun=[]
for i in range(3):
    b=rand.randint(0,100)
    ikincisutun.append(b)
ucuncusutun=[]
for i in range(3):
    c=rand.randint(0,100)
    ucuncusutun.append(c)
matris=[ilksutun,ikincisutun,ucuncusutun] 

print(matris)