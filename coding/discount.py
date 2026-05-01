bill=int(input("enter bill :"))



if bill>5000:
    print(0.85*bill)
elif bill>=1000 and bill<5000:
    print(0.90*bill)

elif bill<1000:
     print(0.95*bill)