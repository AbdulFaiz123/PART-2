#Write a program to accept a number “n” from the user; 
# then display the series 1,3,5,7,9,…,n and 
# find the sum of the numbers in this series.
def series(n):
    lst=[int(i) for i in str(n)]
  
    summ =0
    for j in lst:
       

        summ+= j
        print(f'sum of series {summ}')
        
    
    return summ
n=str(input("enter the number"))
 print(n)
series(n)