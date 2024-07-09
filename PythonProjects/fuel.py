def main():
    while True:
        try:
            fuel = input("Fraction: ")
            x, y = fuel.split("/")
            new_x = int(x)
            new_y = int(y)

            if new_x > new_y:
                continue

            value = new_x / new_y
            percentage = round(float(value * 100))


            if percentage <= 1:
                print("E")
                break
            elif percentage >= 99:
                print("F")
                break
            elif percentage > 100:
                fuel = input("Fraction: ")
            else:
                print(f"{percentage}" + "%")
                break

        except (ValueError, ZeroDivisionError):
            pass
main()
