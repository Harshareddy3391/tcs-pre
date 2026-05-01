"""n=input("enter num :")

s_val=str(n)

check=s_val[::-1]

data=int(check)


if n == data:
    print(f"{n} is palin")
if n == n[::-1]:
    print("palin")"""

"""
n=int(input("enter num :"))

for i in range(n+1):

    i_str=str(i)


    if i_str == i_str[::-1]:
        print(i)
 """

n=int(input())


d=n


s=0
while n>0:

    digit =n%10
    s=s*10+digit

    n=n//10
if s == d :
    print(f"{d} is palin..")

else:
    print("not palin")