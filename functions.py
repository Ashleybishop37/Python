# Temperature calculation function
def temperature_calc(temptype):
    if temptype == "1":
        degrees = float(input("What is the degrees in Celsius? "))
        calc_fahrenheit = (((degrees / 5) * 9) + 32)
        print(f"\033[1;33m {degrees} degrees Celsius is about {calc_fahrenheit:.2f} degrees Fahrenheit \033[0m")
        log(degrees, "degrees celsius", calc_fahrenheit, "fahrenheit", "(((" + str(degrees) + "/ 5) * 9) + 32)")
        end_prompt()

    if temptype == "2":
        degrees = float(input("What is the degrees in Fahrenheit? "))
        calc_celsius = float((((degrees - 32) * 5) / 9))
        print(f"\033[1;33m {degrees} degrees fahrenheit is about {calc_celsius:.2f} degrees Celsius \033[0m")
        log(degrees, " degrees fahrenheit", calc_celsius, "celsius", "(((" + str(degrees) + "- 32) * 5) / 9")
        end_prompt()


# Area calculation function
def area_calc(areaType):
    if areaType == "1":
        sqFoot = float(input("How many Sq Feet? "))
        calcSqMeter = float(sqFoot / 10.764)
        print(f"\033[1;33m {sqFoot} square feet is about {calcSqMeter:.2f} meters \033[0m")
        log(sqFoot, "Sq Feet", calcSqMeter, "Sq Meter", str(sqFoot) + "/ 10.764")
        end_prompt()
    if areaType == "2":
        sqMeter = float(input("How many Sq Meters? "))
        calcSqFoot = float(sqMeter * 10.764)
        print(f"\033[1;33m {sqMeter} Meters is about {calcSqFoot:.2f} square feet \033[0m")
        log(sqMeter, "Sq Meters", calcSqFoot, "Sq Feet", str(sqMeter) + "* 10.764")
        end_prompt()


# Volume calculation function
def volume_calc(volumeType):
    if volumeType == "1":
        liter = float(input("How many Liters? "))
        calcGallon = float(liter / 3.785411784)
        print(f"\033[1;33m {liter} liters is about {calcGallon:.2f} gallons \033[0m")
        log(liter, "liters", calcGallon, "gallons", str(liter) + "/ 3.785411784")
        end_prompt()
    if volumeType == "2":
        gallon = float(input("How many Gallons? "))
        calcLiter = float(gallon * 3.785411784)
        print(f"\033[1;33m {gallon} gallons is about {calcLiter:.2f} liters \033[0m")
        log(gallon, "gallons", calcLiter, "liters", str(gallon) + "* 3.785411784")
        end_prompt()


# Weight calculation function
def weight_calc(weightType):
    if weightType == "1":
        pound = float(input("How many pounds? "))
        calcKilogram = float(pound * 0.45359237)
        print(f"\033[1;33m {pound} pounds is about {calcKilogram:.2f} kilograms \033[0m")
        log(pound, "pounds", calcKilogram, "kilograms", str(pound) + " * 0.45359237")
        end_prompt()
    if weightType == "2":
        kilogram = float(input("How many kilograms? "))
        calcPound = float(kilogram / 0.45359237)
        print(f"\033[1;33m {kilogram} kilograms is about {calcPound:.2f} pounds \033[0m")
        log(kilogram, "kilograms", calcPound, "pounds", str(kilogram) + "/ 0.45359237")
        end_prompt()


# Writing to log file
def log(input, inputLabel, endCalc, calcLabel, calculation):
    calculation_log = f" {input} {inputLabel} = {endCalc} {calcLabel} -> {calculation} \n"
    with open("log.txt", "a") as f:
        f.write(calculation_log)
        f.close()


# Reading most recent 10 calculations (prints with a run # in front of each line)
def read_file():
    N = 10
    line_number = 0
    with open("log.txt", "r") as f:
        for line in (f.readlines()[-N:]):
            line_number = line_number + 1
            print("\033[0;36m Run #" + str(line_number) + ": \033[1;37m" + line, end='')


# Prompt for print history or exit
def end_prompt():
    print("\n 1. Print last 10 runs \n 2. Exit")
    response = input("\033[0;31m Please enter appropriate number(1-2): ")

    if response == "1":
        read_file()

    if response == "2":
        exit()
