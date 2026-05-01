"""a=0
b=1




#print(a,b)



for i in range(6):
    c=a+b

    print(c,end=" ")

    a=b
    b=c

"""


"""
n=int(input("num :"))


a=0
b=1
for i in range(0,n+1):
    print(a,end=" ")

    c=a+b

    a=b
    b=c"""

a,b=0,1

for i in range(10):
    a,b=b,a+b

    print(a,end=" ")