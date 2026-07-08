import twodfigures

while True:
    print("\n1. Square")
    print("2. Circle")
    print("3. Triangle")
    print("4. Rectangle")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 5:
        break

    op = input("Enter Area or Perimeter: ")

    if ch == 1:
        s = float(input("Enter side: "))
        if op == "Area":
            print(twodfigures.square_area(s))
        else:
            print(twodfigures.square_perimeter(s))

    elif ch == 2:
        r = float(input("Enter radius: "))
        if op == "Area":
            print(twodfigures.circle_area(r))
        else:
            print(twodfigures.circle_circumference(r))

    elif ch == 3:
        if op == "Area":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            print(twodfigures.triangle_area(b, h))
        else:
            a = float(input("Enter side1: "))
            b = float(input("Enter side2: "))
            c = float(input("Enter side3: "))
            print(twodfigures.triangle_perimeter(a, b, c))

    elif ch == 4:
        l = float(input("Enter length: "))
        w = float(input("Enter breadth: "))
        if op == "Area":
            print(twodfigures.rectangle_area(l, w))
        else:
            print(twodfigures.rectangle_perimeter(l, w))