import random
print('You have Only 5 Chances to guess the Number.....')
count = 0
x = random.randrange(1, 100)
while 1:
    d = int (input('Guess the Number:'))
    if (d == x):
        print("Congrats...!!")
        break
    if (count == 4):
        print("Sorry ! No chances left")
        print("The number is : ", x)
        break
    count = count + 1
    if (d > x):
        print("Number is less than ", d)
    else:
        print('Number is greater than ', d)
