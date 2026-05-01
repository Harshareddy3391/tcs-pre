n=int(input("enter num :"))


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
