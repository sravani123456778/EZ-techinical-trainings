#program to find sum of digits in a number using for loop
n=int(input(""))
su=0
for i in range(n):
    rem=n%10
    su=su+rem
    n=n//10
print(su)
#another way
n=int(input(""))
temp=n
sum=0
for i in range(1,n,n//10):
    rem=sum+int(temp%10)
    temp=temp//10
print(sum)