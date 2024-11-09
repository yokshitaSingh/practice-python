a=int(input("enter a no."))
if(a>1):
    count=0
    for i in range(1,a+1):
        if a%i == 0:
            count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not A Prime Number")
