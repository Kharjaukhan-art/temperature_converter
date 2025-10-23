# main.py

def celsius_to_fahrenheit(c):
    """Цельсийден Фаренгейтке түрлендіру"""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Фаренгейттен Цельсийге түрлендіру"""
    return (f - 32) * 5/9

if __name__ == "__main__":
    choice = input("Түрлендіру түрін таңдаңыз (C→F немесе F→C): ")

    if choice.lower() == "c→f":
        c = float(input("Цельсий мәнін енгізіңіз: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c)}°F")
    elif choice.lower() == "f→c":
        f = float(input("Фаренгейт мәнін енгізіңіз: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f)}°C")
    else:
        print("Қате таңдау!")
