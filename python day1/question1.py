
# # Get temperature from user
# temp = float(input("Enter temperature: "))

# # Convert Celsius to Fahrenheit
# c_to_f = (temp * 9/5) + 32
# print("Celsius to Fahrenheit:", c_to_f)

# # Convert Fahrenheit to Celsius
# f_to_c = (temp - 32) * 5/9
# print("Fahrenheit to Celsius:", f_to_c)

# c_to_k = (temp - 273.15)
# print("Clesius to Kelvin :" , c_to_k)

# k_to_c = (temp + 273.15)
# print ("Kelvin to Celsius :",k_to_c)



# Question 1

def convert_temperature(value, from_unit, to_unit):
    """Convert between Celsius, Fahrenheit, and Kelvin."""
    
    # First, convert the input to Celsius
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5/9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        return None  # Invalid input

    # Then convert Celsius to the desired output unit
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return (celsius * 9/5) + 32
    elif to_unit == "K":
        return celsius + 273.15
    else:
        return None


while True:
    print("\n=== Temperature Converter ===")
    
    # Ask user which units to convert
    from_unit = input("Convert from (C/F/K): ").upper()
    to_unit = input("Convert to (C/F/K): ").upper()
    
    # Validate units
    if from_unit not in ("C", "F", "K") or to_unit not in ("C", "F", "K"):
        print(" Invalid unit. Please enter C, F, or K.")
        continue

    # Get temperature and validate numeric input
    try:
        temp = float(input("Enter temperature value: "))
    except ValueError:
        print(" Invalid temperature. Please enter a numeric value.")
        continue

    # Do the conversion
    result = convert_temperature(temp, from_unit, to_unit)
    
    if result is None:
        print(" Conversion error.")
    else:
        print(f"\n{temp}°{from_unit} = {result:.2f}°{to_unit}")

    # Ask to run again or quit
    again = input("\nDo you want to convert again? (y/n): ").lower()
    if again != "y":
        print("Goodbye!")
        break




