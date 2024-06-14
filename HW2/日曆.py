year=int(input("Please input Year:"))
month=int(input("Please input month:"))
print("Sun Mon Tue Wed Thr Fri Sat")
c=year//100
y=year-(c*100)
if month==1 or 2:
    c=(year-1)//2
    y=(year-1)-(c*100)
    month=month+12
    first_week_day=(y+(y//4)+(c//4)-(2*c)+(2*month)+((3*(month+1))//5)+2)%7
    print(f"{0:3}"*(first_week_day),end=" ")
else:
    first_week_day=(y+(y//4)+(c//4)-(2*c)+(2*month)+((3*(month+1))//5)+2)%7
    print(f"{0:3}"*(first_week_day),end=" ")
year_type=0
if year%4==0:
    if year%100==0:
        if year%400:
            year_type="leap_year"
        else:
            year_type="nleap_year"
    else:
        year_type="leap_year"
else:
    year_type=="nleap_year"
num_days=0    
if month==1 or 3 or 5 or 7 or 8 or 10 or 12:
    num_days=31
elif month==4 or 6 or 9 or 11:
    num_days=30
elif month==2:
    if year_type=="leap_year":
        num_day=29
    else:
        num_day=28


    


    
