"""h=int(input("enter hours :"))



if h>=5:
    two_h=2*100
    three_h=3*50

    min=h-5

    bal=min*20

    print(two_h+three_h+bal)

elif h>2 and h<5:
        two_h1=2*100
        min1=h-3
        bal1=h*50
        print(two_h1+bal1)
elif h<=2:
      print(h*100)"""


h=int(input("enter hours :"))


if h<=2:
    print(h*100)

elif h<=5:
    bill=(2*100)+(h-2)*50
    print(bill)

elif h>5:
    bill1=(2*100)+(3*50)+(h-5)*20
    print(bill1)