num=int(input('\nPlease enter your number:  '))
count=0
while num>0:
    count=count+1
    num=num//10
print("\nThe number of digits in the number are: "+str(count))