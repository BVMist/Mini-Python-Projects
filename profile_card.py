#Profile Card

name = input("Your name: ").strip()

#Get age.
while True:
    try:
        age = int(input('Your age: '))
        break
    except:
        continue
        
genders = ['m', 'f']
#Get gender.
while True:
    gender = input("Your gender(m/f): ").strip().lower()
    if gender in genders:
        break
    else:
        print("Input should be either m(male) or f(female).")

status = 'Online'
print("Received...")

print(f'\n{"-"*5}Profile Card{"-"*5}')
print(f"Name: {name.title()}")
print(f"Age: {age}")
print(f"Gender: {'Male' if gender == 'm' else 'Female'}")
print(f'Status: {status}')