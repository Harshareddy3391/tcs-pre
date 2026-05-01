"""a=0
b=1




#print(a,b)



for i in range(6):
    c=a+b

    print(c,end=" ")

    a=b
    b=c

"""


a=20
b=30

a,b = b,a

print(a,b)