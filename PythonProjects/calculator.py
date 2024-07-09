def main():
    math = input("Expression: ")
    x, y, z = math.split(" ")

    final = int(x), y, float(z)
    if y == "+":
        final = int(x) + float(z)
        print(float(final))
    elif y == "-":
        final = int(x) - float(z)
        print(float(final))
    elif y == "*":
        final = int(x) * float(z)
        print(float(final))
    elif y == "/":
        final = int(x) / float(z)
        print(float(final))
    elif y == "^":
        final = int(x) ** float(z)
        print(float(final))
    else:
        print(" ")
main()