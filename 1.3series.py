#Write a program to accept a number “n” from the user; find the sum of the series 1/23+1/33+1/43……. +1/n
n=int(input("enter any thing"))

sum=0
for i in range(2,n+1):
    sum=sum+(1/(i*i*i))

print(sum)