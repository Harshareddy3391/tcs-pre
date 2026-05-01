n=int(input("enter number :"))


for i in range(n+1):

    i_len=len(str(i))

    i_str=str(i)

    tem=i
    total=0


    for j in i_str:

        data = int(j) ** i_len
        total +=data
    if total == tem :
        print(tem)