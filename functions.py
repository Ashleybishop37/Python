import sys
import os

# Temperature calculation function
def temperature_calc(temptype):
    if temptype == "1":
        degrees = int(input("What is the degrees in Celsius? "))
        calc_fahrenheit = (((degrees / 5) * 9) + 32)
        print(f"{degrees} degrees Celsius is {calc_fahrenheit} degrees Fahrenheit")
        log(degrees, "celsius", calc_fahrenheit, "fahrenheit", "(((" + str(degrees) + "/ 5) * 9) + 32)")
        Loop()
    if temptype == "2":
        degrees = int(input("What is the degrees in Fahrenheit? "))
        calc_celsius = (((degrees - 32) * 5) / 9)
        print(f"{degrees} degrees fahrenheit is {calc_celsius} degrees Celsius")
        log(degrees, "fahrenheit", calc_celsius, "celsius", "(((" + str(degrees) + "- 32) * 5) / 9")
        Loop()


# Area calculation function
def area_calc(areaType):
    if areaType == "1":
        sqFoot = int(input("How many Sq Feet? "))
        calcSqMeter = sqFoot / 10.764
        print(f"{sqFoot} sqaure feet  is {calcSqMeter} meters")
        log(sqFoot, "Sq Feet", calcSqMeter, "Sq Meter", str(sqFoot) + "/ 10.764")
        Loop()
    if areaType == "2":
        sqMeter = int(input("How many Sq Meters? "))
        calcSqFoot = sqMeter * 10.764
        print(f"{sqMeter} Meters  is {calcSqFoot} square feet")
        log(sqMeter, "Sq Meters", calcSqFoot, "Sq Feet", str(sqMeter) + "* 10.764")
        Loop()

# Volume calculation function
def volume_calc(volumeType):
    if volumeType == "1":
        liter = int(input("How many Liters? "))
        calcGallon = liter / 3.785411784
        print(f"{liter} liters  is {calcGallon} gallons")
        log(liter, "liters", calcGallon, "gallons", str(liter) + "/ 3.785411784")
        Loop()
    if volumeType == "2":
        gallon = int(input("How many Gallons? "))
        calcLiter = gallon * 3.785411784
        print(f"{gallon} gallons  is {calcLiter} liters")
        log(gallon, "gallons", calcLiter, "liters", str(gallon) + "* 3.785411784")
        Loop()


# Weight calculation function
def weight_calc(weightType):
    if weightType == "1":
        pound = int(input("How many pounds? "))
        calcKilogram = pound * 0.45359237
        print(f"{pound} pounds  is {calcKilogram} kilograms")
        log(pound, "pounds", calcKilogram, "kilograms", str(pound) + " * 0.45359237")
        Loop()
    if weightType == "2":
        kilogram = int(input("How many kilograms? "))
        calcPound = kilogram / 0.45359237
        print(f"{kilogram} kilograms  is {calcPound} pounds")
        log(kilogram, "kilograms", calcPound, "pounds", str(kilogram) + "/ 0.45359237")
        Loop()

def log(input, inputLabel, endCalc, calcLabel, calculation):
    calculation_log = f"{input} {inputLabel} = {endCalc} {calcLabel} -> {calculation} \n"
    f = open("log.txt", "a")
    f.seek(0, 0)
    f.write(calculation_log)
    f.close()


def read_file():
    logFile = open("log.txt")
    number_of_lines = 10
    for i in range(number_of_lines):
        line = logFile.readline()
        print("Run #" + str(i + 1) + ": " + str(line))


def Loop():
    print("1. Print last 10 runs \n 2. Exit")
    response = input("Please enter appropriate number(1-2): ")

    if response == "1":
        read_file()

    if response == "2":
        exit()



