#Unit converter

units_length = ['ft', 'inches', 'cm', 'm']
units_mass = ['kg', 'pounds', 'g']

unit_conv_length = {'ft': {'inches': 12, 'cm': 30.48, 'm': 0.305}, 'inches': {'ft': 0.0833, 'cm': 2.54}, 'm': 0.0254, 'cm': {'ft': 0.0328084,'inches': 0.394, 'm': 0.01}, 'm': {'ft': 3.28084, 'inches': 39.37, 'cm': 100}}

unit_conv_mass = {'kg': {'pounds': 2.205, 'g': 1000}, 'pounds': {'kg': 0.454, 'g': 453.592}, 'g':{'kg': 0.001, 'pounds': 0.0022}}


while True:
    while True:
        unit_type = input("Unit type(length or mass): ").strip()
        if unit_type in ['length','mass']:
            break
            
    unit_list = units_length if unit_type == 'length' else units_mass
    unit_conv = unit_conv_length if unit_type == 'length' else unit_conv_mass
    
    while True:
        unit_from = input(f"From({'ft, inches, cm, m' if unit_list == units_length else 'kg, pounds, g'}): ").strip().lower()
        if unit_from in unit_list:
            break
            
    while True:
        possible_units = ''
        for x in unit_list:
            if x!= unit_from:
                possible_units += x + ', '
      
        unit_to = input(f"To({possible_units}): ").strip().lower()
        if unit_to in unit_list:
            break
            
    while True:
        try:
            value = float(input("Input the value: "))
            break
        except:
            print("Invalid input")
    new_val = value*(unit_conv[unit_from][unit_to])     
    print("\n---Converted---")      
    print(f"Old val: {value}{unit_from}")      
    print(f"New val: {new_val}{unit_to}\n")       