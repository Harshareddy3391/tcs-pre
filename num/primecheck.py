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


n=int(input("enter a number :"))

count=0


for j in range(1,n+1):

    if n%j == 0:

        count+=1

if count == 2:
    print(f"{j} is prime number")

else:
    print("not a prime")
    