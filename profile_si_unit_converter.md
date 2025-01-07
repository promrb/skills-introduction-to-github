import length_converter
import mass_converter
import time_converter
import temprature_converter

def print_menu(menu):
     """This function will print everything in the menu."""
     for index, unit in enumerate(menu):
          print(f"{index} --> {unit}")
     print("")

print("**************************")
print("Welcome to my SI Converter")
print("**************************")
print("Supported SI conversion units are:")


si_units = ["Length","Mass","Time","Temperature","Electric Current","Luminous","Amount of Substance"]
print_menu(si_units)


a=int(input("Select conversion option: "))
print("")

match a:
    case 0:
        print("welcome to length converter")
        length_menu = [
             "meter to km",
             "meter to cm",
             "meter to mm",
             "meter to micrometer",
             "meter to nanometer",
             "meter to miles",
             "meter to yards",
             "meter to foot",
             "meter to inch",
             "meter to light year"
             ]
        print_menu(length_menu)
        length_converter.length_conversion()
    case 1:
        print("welcome to mass converter")
        mass_menu = [
             "kg to gram",
             "kg to miligram",
             "kg to metric ton",
             "kg to long ton",
             "kg to short ton",
             "kg to pound",
             "kg to ounce",
             "kg to carrat",
             "kg to atomic mass unit",    
          ] 
        print_menu(mass_menu)
        mass_converter.mass_conversion()
    case 2:
        print("welcome to time converter")
        time_menu = [
            "second to millisecond",
            "second to nanosecond",
            "second to microsecond",
            "second to minute",
            "second to hour",
            "second to day",
            "second to week",
            "second to month",
            "second to calender year",
            "second to decade",
            "second to century",
        ]
        print_menu(time_menu)
        time_converter.time_conversion()
    case 3:
        print("welcome to temperature converter")
        temprature_menu = [
            "celsius to kelvin",
            "celsius to farenheit",
            ]
        print_menu(temprature_menu)
        temprature_converter.temprature_conversion()
    case 4:
        print("welcome to electric current converter")
    case 5:
        print("welcome to Luminous converter")
    case 6:
        print("welcome to amount of substance converter")
    case _:
        print("Match not found")
