def main():
    a = input("What is a? ")
    while a.isalpha():
        print("Please type in a digit!")
        a = input("What is a? ")

    b = input("What is b? ")
    while b.isalpha():
        print("Please type in a digit!")
        b = input("What is b? ")

    c = input("What is c? ")
    while c.isalpha():
        print("Please type in a digit!")
        c = input("What is c? ")

    formula1 = ((-(float(b))) + ((((float(b))**2) - (4 * (float(a))*(float(c))))**0.5))/(2*(float(a)))
    formula2 = ((-(float(b))) - ((((float(b))**2) - (4 * (float(a))*(float(c))))**0.5))/(2*(float(a)))

    if float(formula1) != float(formula2):
        print(f"Possible answers are {float(formula1):.3f} and {float(formula2):.3f}")
    else:
        print(f"The only possible answer is {float(formula1):.3f}")
        
                
        



           


if __name__ == "__main__":
    main()