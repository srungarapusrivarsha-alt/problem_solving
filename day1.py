amount=int(input("enter amount:"))
chocolate_rate=int(input("enter chocolate rate :"))
purchased_chocolates=amount//chocolate_rate
remaining_change=amount%purchased_chocolates
print("no of chocolates purchased:",purchased_chocolates)
print("remaining_change:",remaining_change)

units=int(input("enter no of units: "))
current_bill=0
if units<=10:
    current_bill=units*5
    print("bill is:",current_bill)
elif units<=50:
    bill=10*5+(units-10)*10
    print("bill is :",bill)
else :
    bill=10*5+40*10+(units-50)*12
    print("bill",bill)

n=int(input("enter a number"))
count=0
while n>0:
    new_number=n//10
    count+=1
print(count)
square=n*n

n=int(input("enter a number"))
temp=n
square=n**2
p=1
while temp>0:
    p=p*10
    temp=temp//10
if square%p==n:
    print("Automorphic number")
else:
    print("not Automorphic number")
