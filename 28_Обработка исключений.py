try:
    x, y = map(int, input().split())
    res = x / y
except ValueError:
    print("Ошибка типа данных!!")
except ZeroDivisionError:
    print("Деление на ноль!")
except:
    print("Любое исключение!!!")

print("Штатное завершение!")
