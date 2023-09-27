#write a program to find ssum of digits using while loop
n=int(input(""))
su=0
while(n>0):
    rem=n%10
    su=su+rem
    n=n//10
print(su)