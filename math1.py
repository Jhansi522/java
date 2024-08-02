# Set A=[-6,-4,0,2,5,7,11,12,17,19,27,31]
Set_A=[-6,-4,0,2,5,7,11,12,17,19,27,31]
for value in (Set_A):
    if value>2:
        for n in range(2,value):
            if value%n == 0:
                print(value)
                break
   
