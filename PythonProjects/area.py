def main():
    height = input("Height: ")
    while height.isalpha():
        print("Please type in a digit!")
        height = input("Height: ")
    else:
        length = input("Length: ")
        while length.isalpha():
            print("Please type in a digit!")
            length = input("Length: ")
        else:
            radius = input("Radius: ")
            while radius.isalpha():
                print("Please type in a digit!")
                radius = input("Radius: ")
            else:
                if radius == 0 and float(height) == float(length):
                    area = float(height) ** 2
                    print(f"The shape is a square and the area is {float(area):.1f}")
                elif radius == 0 and float(height) > float(length) or float(height) < float(length):
                    shape = input(
                        "Is the shape rectangle or triangle? "
                    )  # triangle assumed here is right-angled
                    while shape.isdigit():
                        print("Invalid shape!")
                        shape = input("Is the shape rectangle or triangle? ")
                    else:
                        if shape == "rectangle":
                            area = float(height) * float(length)
                            print(
                                f"The shape is a rectangle and the area is {float(area):.1f}"
                            )
                        elif shape == "triangle":
                            area = (float(height) * float(length)) * 0.5
                            print(
                                f"The shape is a triangle and the area is {float(area):.1f}"
                            )
                        else:
                            shape = input("Is the shape rectangle or triangle? ")
                elif float(height) == 0 and float(length) == 0:
                    shape = input("Is the shape circle or semi-circle? ")
                    while shape != "circle" or shape != "semi-circle":
                        print("Circle or semi-circle?")
                        shape = input("Is the shape circle or semi-circle? ")
                    else:
                        if shape == "circle":
                            area = 3.142 * (float(radius) ** 2)
                            print(
                                f"The shape is a circle and the area is {float(area):.1f}"
                            )
                        else:
                            area = (3.142 * (float(radius) ** 2)) * 0.5
                            print(
                                f"The shape is a semi-circle and the area is {float(area):.1f}"
                            )


if __name__ == "__main__":
    main()
