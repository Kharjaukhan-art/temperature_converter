from calculator import calculator  # Егер функцияны импорттап отырсаң

# Ескерту: input() қолданатын функцияны тікелей тестілеу қиын, 
# сондықтан оны қайта жазып, аргументпен жұмыс істеу ыңғайлы болады.
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

print("Барлық тесттер өтті!")
