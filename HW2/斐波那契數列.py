n=int(input("Input an integer number:"))
arr=[]
i=0
while i<(n+1):
  if i==0:
    arr=[0]
  elif i==1:
    arr=[0,1]
  else:
    arr.append(arr[i-1]+arr[i-2])
  i=i+1
if n==1:
  print(arr[0])
else:
  print(arr[n])
