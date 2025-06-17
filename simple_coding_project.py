"""Standalone temperature converter script."""

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

if __name__ == "__main__":
    c = 25
    f = 77
    print(f"{c}°C is {celsius_to_fahrenheit(c):.2f}°F")
    print(f"{f}°F is {fahrenheit_to_celsius(f):.2f}°C")
