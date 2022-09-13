try:
    # x, y = map(int, input().split())
    # res = x / y
    with open("myfile.txt", "w") as f:
        f.write("Hello!\n")
except ValueError as z:
    print(z)
except ZeroDivisionError as z:
    print(z)
except:
    print("Любое исключение!!!")
else:
    print("Иключений не произошло (__:))")
finally:
    # print("Блок finally выполняется всегда!")
    if f:
        f.close()
        print(f"Файл закрыт.")
