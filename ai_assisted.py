# CSE325-2026-L01-K7QX-T2

RUN_PROFILE = "ai"


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


def main():
    try:
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}C = {fahrenheit}F")
    except ValueError:
        print("Please enter a valid numeric temperature.")


if __name__ == "__main__":
    main()