#Age Calculator
import datetime as dt

date = dt.date.today()
while True:
    while True:
        try:
            year = int(input("Please input birth year: "))
            break
        except:
            continue
        
    while True:
        try:
            month = int(input("Please input birth month: "))
            break
        except:
            continue
        
    while True:
        try:
            day = int(input("Please input birth day: "))
            break
        except:
            continue
        
        

    try:
        birthdate = dt.date(year, month, day)
        break
    except:
        print("Invalid date.")
        continue
   
        
#Calculating age..                  
age = date.year - birthdate.year
if birthdate.month >= date.month:
    if birthdate.month > date.month:
        age = age - 1
    elif birthdate.day > date.day:
        age = age - 1

                
print("Age: ", age)