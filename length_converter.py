# Utilities
def input_number(unit):
    a=input(f"Enter a number to convert from meter to {unit}: ")
    return a


def print_output(input, input_num, output, output_number):
    print("=================================")
    print(f"     {input_num} {input} == {output_number} {output}")
    print("=================================")
# Conversion from meter to unit
def meter_to_km():
    meters = input_number("km")

    km = (int(meters) / 1000)

    print_output("meters", meters, "km", km)

def meter_to_cm():

    meters = input_number("from meter to cm")
    
    cm = (int(meters) * 100)

    print_output("meters", meters, "cm", cm)


def meter_to_mm():
    
    meters = input_number("mm: ")

    mm = (int(meters) * 1000)

    print_output("meters", meters, "mm", mm)


def meter_to_micrometer():
    
    meters = input_number("micrometer: ")

    micrometer = (int(meters) * 1000000)

    print_output("meters", meters, "micrometers", micrometer)


def meter_to_nanometer():

    meters = input_number("nanometer: ")

    nanometer = (int(meters) * 1000000000)

    print_output("meters", meters, "nanometers", nanometer)


def meter_to_mile():

    meters = input_number("miles: ")

    miles = (int(meters) / 1609.35)   

    print_output("meters", meters, "miles", miles)


def meter_to_yards():

    meters = input_number("yards: ")

    yards = (int(meters) * 1.09361)

    print_output("meters", meters, "yards", yards)


def meter_to_foot():

    meters = input_number("foot: ")

    foot = (int(meters) * 3.28084)

    print_output("meters", meters, "foot", foot)

    foot = (int(meters) / 1000)
    print("in km it is")
    print_output("meters", meters, "foot", foot)

    foot = (int(meters) * 1000)
    print("in mm it is")
    print_output("meters", meters, "foot", foot)


def meter_to_inch():

    meters = input_number("inch: ")

    inch = (int(meters) * 39.26)

    print_output("meters", meters, "inch", inch)


def meter_to_light_year():

    meters = input_number("light year: ")

    light_year = (int(meters) / 1.057e-16)

    print_output("meters", meters, "light_year", light_year)
    
# Main call
def length_conversion():
    a=input("Select conversion option: ")
    if a=="0":
        print("welcome to meter to km")
        meter_to_km()
    elif a == "1":
        print("Welcome to meter to cm")
        meter_to_cm()
    elif a=="2":
        print("welcome to meter to mm")
        meter_to_mm()
    elif a=="3":
        print("welcome to meter to micrometer")
        meter_to_micrometer()
    elif a=="4":
        print("welcome to meter to nanometer")
        meter_to_nanometer()
    elif a=="5":
        print("welcome to meter to miles")
        meter_to_mile()
    elif a=="6":
        print("welcome to meter to yards")
        meter_to_yards()
    elif a=="7":
        print("welcome to meter to foot")
        meter_to_foot()
    elif a=="8":
        print("welcome to meter to inch")
        meter_to_inch()
    elif a=="9":
        print("welcome to meter to light year")
        meter_to_light_year()
    else:
        print("Match not found")
