"""n = int(input())

if n <= 1:
    print("Not Prime")
else:
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break

    print("Prime" if flag else "Not Prime")"""

"""
n=int(input("enter a number :"))

count=0


for j in range(1,n+1):

    if n%j == 0:

        count+=1

if count == 2:
    print(f"{j} is prime number")

else:
    print("not a prime")
    """

"""

for i in range(1,101):

    if i>1:

        for j in range(2,int(i**0.5)+1):

            if i%j == 0:
                break

        else:
            print(i)



for i in range(1,200):
    if i>1:
        for h in range(2,int(i**0.5)):
            if i%h == 0:
                break
        else:
            print(i)    """
#practice



"""
n=int(input("Enter your number :"))

 



for j in range(1,n+1):
    c=0

    for s in range(1,j+1):

        if j%s== 0:

            c +=1

    if c == 2:
        print(f"{j}",end=" ")"""

n=int(input("num"))

"""
for i in range(1,n+1): 
    count=0
    for j in range(1,i+1):

        if i%j == 0:
            count +=1
    if count == 2 :
        print(i,end=" ")    """

for s in range(2,n+1):

    for j in range(2,int(s**0.5)+1):


        if s%j == 0:

            break
    else:
        print(s,end=" ")

