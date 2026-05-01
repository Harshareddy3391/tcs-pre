"""n=int(input("enter num :"))


sum_n=0

product=1


while n>0:

    digit=n%10
    sum_n += digit
    product *=digit

    n //=10

if sum_n == product :
    print("spy number")

else:
    print("not spy")
"""


#n=int(input("enter :"))



#tem=n

#sval=0
#pval=1

"""
for i in str(n):
    sval +=int(i)
    pval *=int(i)

if sval == pval :
    print(f"{n} is spy")

else:
    print(f"{n}not spy")



    """

"""
while n>0:
    digit = n%10
    sval +=digit
    pval *=digit

    n //= 10

if sval == pval :
    print(f"{tem} is spy")

else:
    print(f"{tem}not spy")"""



n=int(input("enter :"))

for i in range(0,n+1):
    temp=i

    sum_data=0
    product=1
    

    for j in str(i):


        sum_data +=int(j)

        product *=int(j)

    if sum_data == product :
        print(f"{temp} is spy")
    