from heron import func

if __name__ == "__main__":
    s = input("Введите три стороны треугольника: ").strip()
    a, b, c = map(float, s.split())
    print(f"Площадь треугольника со сторонами {a}, {b}, {c} = {func(a,b,c)}")

