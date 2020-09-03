from Functions import temperature_calc,area_calc,volume_calc,weight_calc

print(" \033[0;34m Welcome! What kind of conversion are you looking to do?")
print(" \033[1;37m Here are your options: \n 1. Temperature \n 2. Area \n 3. Volume \n 4. Weight")
conversionType = input(" \033[0;31m Enter the appropriate number(1-4): ")

if conversionType == "1":
    print(" \033[0;34m \n You chose a TEMPERATURE conversion")
    print(" \033[1;37m Please specify the direction of the conversion: \n 1. Celsius to Fahrenheit \n 2. Fahrenheit to Celsius")
    tempType = input(" \033[0;31m Enter the appropriate number(1-2): \033[1;37m")
    if tempType == "1" or tempType == "2":
        temperature_calc(tempType)

if conversionType == "2":
    print(" \033[0;34m \n You chose a AREA conversion")
    print(" \033[1;37m Please specify the direction of the conversion:")
    print("1. Square Foot to Square Meter \n2. Square Meter to Square Foot")
    areaType = input(" \033[0;31m Enter the appropriate number(1-2): \033[1;37m")
    if areaType == "1" or areaType == "2":
        area_calc(areaType)

if conversionType == "3":
    print(" \033[0;34m \n You chose a VOLUME conversion")
    print(" \033[1;37m Please specify the direction of the conversion: \n 1. Liter to Gallon  \n 2. Gallon to Liter")
    volumeType = input(" \033[0;31m Enter the appropriate number(1-2): \033[1;37m")
    if volumeType == "1" or volumeType == "2":
        volume_calc(volumeType)

if conversionType == "4":
    print(" \033[0;34m \n You chose a WEIGHT conversion")
    print("\033[1;37m Please specify the direction of the conversion: \n 1. Pound to Kilogram \n 2. Kilogram to Pound")
    weightType = input(" \033[0;31m Enter the appropriate number(1-2): \033[1;37m")
    if weightType == "1" or weightType == "2":
        weight_calc(weightType)
