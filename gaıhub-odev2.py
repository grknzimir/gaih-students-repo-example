namesurname=[]
point=[]
ortpoint=[]
for i in range(5):
    a=str(input("öğrenci adı soyadı giriniz:"))
    namesurname.append(a)
    for k in range(3):
        b=int(input("öğrenci M-F-H notları:"))
        point.append(b)
print("adsoyadlar:", namesurname)
print("notlar:", point)

for j in range(5):
    
    dict={namesurname[j]:[point[j],point[j+1],point[j+2]]}
    print(dict)
    ort=(point[j]+point[j+1]+point[j+2])/3
    ortpoint.append(ort)
print("notların ortalamaları:",ortpoint)
enyüksek=0
for g in range(5):
    if ortpoint[g]>enyüksek:
        enyüksek=ortpoint[g]
print("en iyi öğrenci ortalaması:",enyüksek)





