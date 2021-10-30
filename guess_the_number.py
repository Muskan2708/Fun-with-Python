import  random
nump=random.randint(1000,9999)
n=int(input("enter a number: "))
while n!=10:
    num=nump
    cor=0
    while num%10:
        numc=num%10
        nc=n%10
        num//=10
        n//=10
        if numc==nc:
            cor+=1
    if cor==4:
        print("CONGRATSSSS!!!! YOU GUESSED ALL THE DIGITS ")
        print("Hey this is FUN... Wanna do it again??")
    else:
        print("You guessed %d digits right"%cor)
        print("No Worries, Let's try it again....")
    n = int(input("enter a number: "))
else:
    print('You Quit the game.... See You Next Time')