# 1.🧙‍♂️ The Magic Number
n=int(input("enter a number"))
while n>=10:
    digit_sum=0
    while n>0:
        last_digit=n%10
        digit_sum=digit_sum+last_digit
        n=n//10
    n=digit_sum   
print("The magic number is:",n)

# 2.🚗 Lucky Car Number
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
# 2.🚗 Lucky Car Number
n=int(input("enter a  number: "))
digital_root=((n-1)%9)+1
print(digital_root)
if digital_root==7:
    print("lucky number")
else:
    print("not a lucky number")

# 3. 🏆 Tournament Player ID
player_id=int(input("enter player id :"))
while player_id>=10:
    digital_root=0
    while player_id>0:
        last_val=player_id%10
        digital_root=digital_root+last_val
        player_id=player_id//10
    player_id=digital_root
print("digital root is :",digital_root)

# 4. 🔐 Secret Door Code
secret_code=int(input("enter secret code:"))
while secret_code>=10:
    digital_root=0
    while secret_code>0:
        last_val=secret_code%10
        digital_root=digital_root+last_val
        secret_code=secret_code//10
    secret_code=digital_root
print("digital code is :",digital_root)
if digital_root%2==0:
    print("door opened")
else:
    print("door locked")

# 5. 💰 Treasure Hunter
treasure=int(input("enter treasure number:"))
while treasure>=10:
    special_treasure=0
    while treasure>0:
        last_val=treasure%10
        special_treasure=last_val+special_treasure
        treasure=treasure//10
    treasure=special_treasure
print("special treasure:",special_treasure)
if special_treasure==9:
    print("💰 special treasure..")
else:
    print("💰 not a special treasure")

# 6. 🐉 Dragon Energy

n=int(input("enter energy value :"))
while n>=10:
    digit_val=0
    while n>0:
        last_val=n%10
        digit_val=last_val+digit_val
        n=n//10
    n=digit_val
print(digit_val)

# 7. 🎟️ Lucky Ticket 
n=int(input("enter a number:"))
k=6
digital_root=((n-1)%9)+1
print(digital_root)
if digital_root==k:
    print("lucky ticket")
else:
    print("not a lucky ticket")
        
