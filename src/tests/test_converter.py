
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from temperature_converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit,
)

class TestTemperatureConversion(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40.0)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(celsius_to_kelvin(0), 273.15)
        self.assertAlmostEqual(celsius_to_kelvin(100), 373.15)
        self.assertAlmostEqual(celsius_to_kelvin(-273.15), 0.0)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0.0)
        self.assertAlmostEqual(kelvin_to_celsius(373.15), 100.0)
        self.assertAlmostEqual(kelvin_to_celsius(0), -273.15)

    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(fahrenheit_to_kelvin(32), 273.15)
        self.assertAlmostEqual(fahrenheit_to_kelvin(212), 373.15)
        self.assertAlmostEqual(fahrenheit_to_kelvin(-459.67), 0.0)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(kelvin_to_fahrenheit(273.15), 32.0)
        self.assertAlmostEqual(kelvin_to_fahrenheit(373.15), 212.0)
        self.assertAlmostEqual(kelvin_to_fahrenheit(0), -459.67, places=2)

def test_celsius_to_fahrenheit_pytest():
    import pytest
    assert celsius_to_fahrenheit(0) == pytest.approx(32.0)
    assert celsius_to_fahrenheit(100) == pytest.approx(212.0)
    assert celsius_to_fahrenheit(-40) == pytest.approx(-40.0)

def test_fahrenheit_to_celsius_pytest():
    import pytest
    assert fahrenheit_to_celsius(32) == pytest.approx(0.0)
    assert fahrenheit_to_celsius(212) == pytest.approx(100.0)
    assert fahrenheit_to_celsius(-40) == pytest.approx(-40.0)

def test_celsius_to_kelvin_pytest():
    import pytest
    assert celsius_to_kelvin(0) == pytest.approx(273.15)
    assert celsius_to_kelvin(100) == pytest.approx(373.15)
    assert celsius_to_kelvin(-273.15) == pytest.approx(0.0)

def test_kelvin_to_celsius_pytest():
    import pytest
    assert kelvin_to_celsius(273.15) == pytest.approx(0.0)
    assert kelvin_to_celsius(373.15) == pytest.approx(100.0)
    assert kelvin_to_celsius(0) == pytest.approx(-273.15)

def test_fahrenheit_to_kelvin_pytest():
    import pytest
    assert fahrenheit_to_kelvin(32) == pytest.approx(273.15)
    assert fahrenheit_to_kelvin(212) == pytest.approx(373.15)
    assert fahrenheit_to_kelvin(-459.67) == pytest.approx(0.0)

def test_kelvin_to_fahrenheit_pytest():
    import pytest
    assert kelvin_to_fahrenheit(273.15) == pytest.approx(32.0)
    assert kelvin_to_fahrenheit(373.15) == pytest.approx(212.0)
    assert kelvin_to_fahrenheit(0) == pytest.approx(-459.67)
