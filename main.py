def celsius_to_fahrenheit(c):
    """Цельсийден Фаренгейтке түрлендіру"""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Фаренгейттен Цельсийге түрлендіру"""
    return (f - 32) * 5/9

def print_welcome():
    print("Температура түрлендіру қосымшасына қош келдіңіз!")

def convert_temperature():
    while True:
        choice = input("\nТүрлендіру түрін таңдаңыз (C→F немесе F→C, шығу үшін Q): ").strip().lower()
        
        if choice == "c→f":
            try:
                c = float(input("Цельсий мәнін енгізіңіз: "))
                print(f"{c}°C = {celsius_to_fahrenheit(c)}°F")
            except ValueError:
                print("Қате! Сан енгізіңіз.")
        elif choice == "f→c":
            try:
                f = float(input("Фаренгейт мәнін енгізіңіз: "))
                print(f"{f}°F = {fahrenheit_to_celsius(f)}°C")
            except ValueError:
                print("Қате! Сан енгізіңіз.")
        elif choice == "q":
            print("Бағдарлама аяқталды. Сау болыңыз!")
            break
        else:
            print("Қате таңдау! Тек 'C→F', 'F→C' немесе 'Q' енгізіңіз.")

if __name__ == "__main__":
    print_welcome()
    convert_temperature()


