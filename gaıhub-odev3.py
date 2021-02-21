def first_function(data):
    if data>1:
        for k in range(2,data):
            if (data % k)==0:
                break
        else:
                print("sayı asaldır:",data)
def second_function(data): 
    if data>1:
        for j in range(2,data):
            if (data % j)==0:
                break
        else:
                print("sayı asaldır:",data)

for i in range(1000):
    if i<500:
        first_function(i)
    elif 500<=i<1000:
        second_function(i)
    else:
        print("0-1000 sayı arasında hiç asal sayı yoktur.")

