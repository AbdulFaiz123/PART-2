#Write a program to print the Fibonacci series up to the number 34. (Example: 0,1,1,2,3,5,8, 13,… The Fibonacci series starts with 0 and 1, and the succeeding numbers of the series are arrived at by adding the previous 2 numbers.)

a=0
b=1
c=0
print(a,b,end=" ")
while not c==34:
    c=a+b
    print(c,end="")
    a,b=b,c