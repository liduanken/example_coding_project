# Temperature Converter

This is a simple Python script that converts temperatures between Celsius, Fahrenheit and Kelvin.

## Features

- Convert Celsius to Fahrenheit
- Convert Fahrenheit to Celsius
- Convert Celsius to Kelvin and vice versa
- Convert Fahrenheit to Kelvin and vice versa
- Includes example usage in the main block

## Usage

Run the script directly:

```bash
python src/temperature_converter/convert.py
```

You can also import the conversion functions from the package:

```python
from temperature_converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit,
)
```

Example output:

```
25°C is 77.00°F
77°F is 25.00°C
0°C is 273.15K
300K is 80.33°F
```

## Functions

- `celsius_to_fahrenheit(celsius)`
  Converts Celsius to Fahrenheit.

- `fahrenheit_to_celsius(fahrenheit)`
  Converts Fahrenheit to Celsius.

- `celsius_to_kelvin(celsius)`
  Converts Celsius to Kelvin.

- `kelvin_to_celsius(kelvin)`
  Converts Kelvin to Celsius.

- `fahrenheit_to_kelvin(fahrenheit)`
  Converts Fahrenheit to Kelvin.

- `kelvin_to_fahrenheit(kelvin)`
  Converts Kelvin to Fahrenheit.

## Requirements

- Python 3.x
  No external libraries are required.
- pytest for running tests
