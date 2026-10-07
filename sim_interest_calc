#Simple Interest Calculator

def calc(p, r, t):
    simple_interest = (p*r*t)/100
    return simple_interest
    
while True:
    try:
        principal = float(input("Principal: "))
        break
    except:
        print("Invalid input.")
        
while True:
    try:
        rate = float(input("Rate: "))
        break
    except:
        print("Invalid input.")
        
while True:
    try:
        time = float(input("Time: "))
        break
    except:
        print("Invalid input.")
 
interest = calc(principal, rate, time)               
print("\nSimple Interest:", interest)
print("Amount:", principal + interest)