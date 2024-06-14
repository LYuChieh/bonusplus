print(" "," ","a"," ","b"," ","c"," ","d"," ","e"," ","f"," ","g"," ","h"," ","i")
l=["+"]*10
print(" ","---".join(l))
for i in range(1,10):
    print(str(i),"   ".join(["|"]*10),"\n","","---".join(l))
