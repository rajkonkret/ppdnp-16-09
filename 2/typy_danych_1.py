import sys
from email.quoprimime import body_length

wiek = 47
rok = 2024
temp = 36.6  # float

print(temp)
print(type(temp))  # <class 'float'>, zmiennoprzecinkowe

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # 0.023221343873517788 float

print(wiek // rok)  # częśc całkowita z dzielenia 0
print(rok // wiek)  # częśc całkowita z dzielenia, 43

print(rok % wiek)  # reszta z dzielenia (modulo) wynik 3
print(5 % 2)  # reszta 1 bo 2 * 2 + 1 = 5

print(wiek ** rok)  # potęgowanie 47^2024

# len() - długość
print(len(str(wiek ** rok)))  # długość 3385 znaków
# print(len(str(wiek ** rok ** 2)))  # długość 3385 znaków
# ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)
print(54 - 5 * 43 + (4 / 2 + 4) / 2)
# -157.0
# -158.0

# przy float mamy bład zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.34
# Wartość liczby zmiennoprzecinkowej jest obliczana według wzoru:
# x=SMBE,
# {\displaystyle x=SMB^{E},}
# gdzie:
# S {\displaystyle S} (ang. sign) – znak liczby, 1 lub −1,
# M {\displaystyle M} (ang. mantissa) – znormalizowana mantysa, liczba ułamkowa[1],
# B {\displaystyle B} (ang. base) – podstawa systemu liczbowego[1] (2 dla systemów komputerowych),
# E {\displaystyle E} (ang. exponent) – wykładnik, cecha, liczba całkowita[1].
print(sys.float_info)
# sys.float_info(
#     max=1.7976931348623157e+308,
#     max_exp=1024,
#     max_10_exp=308,
#     min=2.2250738585072014e-308,
#     min_exp=-1021, min_10_exp=-307,
#     dig=15,
#     mant_dig=53,
#     epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(f"Sprawdzenie zmiennej {temp} {wiek}")  # Sprawdzenie zmiennej 36.6 47
print(f"""
{wiek}
{temp}""")
# 47
# 36.6

# typ logiczny
# prawdda, fałsz
# True, False
# 1 - prawda, 0  - fałsz
czy_znasz_pythona = True
print(czy_znasz_pythona)
print(type(czy_znasz_pythona))  # <class 'bool'>

print(int(czy_znasz_pythona))  # 1
print(int(False))  # 0

print(bool(1))  # True
print(bool(100))
print(bool(-100))
print(bool(-6.8))
print("radek")
print(bool(" "))  # True
# True
# True
# True
# True
# radek

print(bool(0))
print(bool(""))
# False
# False

print(bool(None))  # False, None - nic, stan nnieokreslony, odpowiednik null

# działania logiczne
# and -> i
print(True and True)  # True
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False

# or - lub
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not - negacja
print(not True)  # False
print(not False)  # True

a = 8
b = 6

print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 8 > 6 = True
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 8 < 6 = False
print(f"Porównanie {a <= b=}")  # Porównanie a <= b=False
print(f"Porównanie {a >= b=}")  # Porównanie a >= b=True
print(f"Porównanie {a} == {b} = {a == b}")  # Porównanie 8 == 6 = False, == - prównanie
print(f"Porównanie {a} != {b} = {a != b}")  # czy różne, Porównanie 8 != 6 = True
print(f"{a=}")  # a=8
