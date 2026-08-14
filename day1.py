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

units = int(input("Enter no of units: "))

cost1 = int(input("Enter cost for first 10 units: "))
cost2 = int(input("Enter cost for 11 to 50 units: "))
cost3 = int(input("Enter cost above 50 units: "))
if units<=10:
    bill=units*cost1
    print(bill)
elif units<=50:
    bill=(10*cost1)+(units-10)*cost2
    print(bill)
else:
    bill=(10*cost1)+(40*cost2)+((units-50)*cost3)
    print(bill)