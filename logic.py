
from Functions import temperature_calc,area_calc,volume_calc,weight_calc

print("Welcome! What kind of conversion are you looking to do?")
print("Here are your options: \n 1. Temperature \n 2. Area \n 3. Volume \n 4. Weight")
conversionType = input("Enter the appropriate number(1-4): ")

if conversionType == "1":
    print("You chose a TEMPERATURE conversion")
    print(" \n Please specify the direction of the conversion: \n 1. Celsius to Fahrenheit \n 2. Fahrenheit to Celsius")
    tempType = input("Enter the appropriate number(1-2): ")
    if tempType == "1" or tempType == "2":
        temperature_calc(tempType)


if conversionType == "2":
    print("You chose a AREA conversion")
    print("\n Please specify the direction of the conversion:")
    print("1. Square Foot to Square Meter \n 2. Square Meter to Square Foot")
    areaType = input("Enter the appropriate number(1-2): ")
    if areaType == "1" or areaType == "2":
        area_calc(areaType)

if conversionType == "3":
    print("You chose a VOLUME conversion")
    print("\n Please specify the direction of the conversion: \n 1. Liter to Gallon  \n 2. Gallon to Liter")
    volumeType = input("Enter the appropriate number(1-2): ")
    if volumeType == "1" or volumeType == "2":
        volume_calc(volumeType)

if conversionType == "4":
    print("You chose a WEIGHT conversion")
    print("\n Please specify the direction of the conversion: \n 1. Pound to Kilogram \n 2. Kilogram to Pound")
    weightType = input("Enter the appropriate number(1-2): ")
    if weightType == "1" or weightType == "2":
        weight_calc(weightType)

