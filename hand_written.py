# CSE325-2026-L01-K7QX-T1

RUN_PROFILE = "manual"


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    c = float(input("Celsius: "))
    print(f"{c}C = {celsius_to_fahrenheit(c)}F")