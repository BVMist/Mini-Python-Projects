#Receipt Total

bill = 0

print("Input price of individual items purchased, individually.")
print("Input 'done' to stop.")
while True:
    price = input("Price: ").strip().lower()
    if price != 'done':
        try:
            bill += int(price)
        except:
            print("Invalid")
    else:
        break
        
print(f"Total: {bill}")                  