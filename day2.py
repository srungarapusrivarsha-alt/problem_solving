n=int(input("enter a number"))
while n>=10:
    digit_sum=0
    while n>0:
        last_digit=n%10
        digit_sum=digit_sum+last_digit
        n=n//10
    n=digit_sum   
print("The magic number is:",n)

number=int(input("enter car registration number: "))
while number>=10:
    digital_root=0
    while number>0:
        last_digit=number%10
        digital_root=digital_root+last_digit
        number=number//10
    n=digital_root
    if n==7:
        print("lucky car")
    else:
        print("not a lucky car")
print(digital_root)

n=int(input("enter a  number: "))
digital_root=((n-1)%9)+1
print(digital_root)
if digital_root==7:
    print("lucky number")
else:
    print("not a lucky number")

n=int(input("enter a number:"))
k=6
digital_root=((n-1)%9)+1
print(digital_root)
if digital_root==k:
    print("lucky ticket")
else:
    print("not a lucky ticket")


