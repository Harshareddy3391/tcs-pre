n=int(input("Enter number :"))

temp=n

sumnu=0

product=1


while n>0:

    digit =n%10

    sumnu +=digit
    product *=digit

    n //=10

if product == sumnu:
    print(f"{temp} spy number")
else:
    print(f"{temp} not spy")