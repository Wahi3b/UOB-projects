import random
initial_money = int(input("Please enter the initial value of entry money:"))
count = 0
total = initial_money
max = initial_money
while True:
    count += 1
    first_dice = random.randint(0, 6)
    second_dice = random.randint(0, 6)
    print (first_dice,second_dice)
    if first_dice + second_dice == 7 :
        total += 4
        if max < total:
            max = total
    else :
        total -= 1 
    if total == 0 :
        break
print(count)
print(max)


