# Simple Coding Project: Temperature Converter

# This script converts temperatures between Celsius and Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Example usage
if __name__ == "__main__":
    c = 25
    f = 77
    print(f"{c}°C is {celsius_to_fahrenheit(c):.2f}°F")
    print(f"{f}°F is {fahrenheit_to_celsius(f):.2f}°C")
