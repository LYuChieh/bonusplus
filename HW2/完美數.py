r=int(input("Input the range number: "))
print("Perfect number:")
n=2
while n<r:
    i=1
    sum=0
    while i<n:
        if n%i==0:
            sum=sum+i
        i=i+1
    if sum==n:
        print(n)
    n=n+1    
