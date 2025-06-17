# Simple Coding Project: Temperature Converter

# This script converts temperatures between Celsius, Fahrenheit and Kelvin

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

# Example usage
if __name__ == "__main__":
    c = 25
    f = 77
    print(f"{c}°C is {celsius_to_fahrenheit(c):.2f}°F")
    print(f"{f}°F is {fahrenheit_to_celsius(f):.2f}°C")
