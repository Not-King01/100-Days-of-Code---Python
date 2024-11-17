import art
print(art.logo)
def add(n1, n2):
    return n1 + n2

def mul(n1, n2):
    return n1 * n2

def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    return n1 / n2

cal = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}
a = float(input("Enter first number: "))
b = input("Enter the operation to be performed(+, -, *, /): ")
if b == '+' or b == '-' or b == '*' or b == '/':
    c = float(input("Enter second number: "))
    d = cal[b](a, c)
    print(d)
else:
    print("Enter a valid operation!!")

while True:
    y_or_n = input("Would you like to continue? (y/n): ")
    if y_or_n == "y":
        con_or_new = input("Would you like to have the previous calculation as first number? (y/n): ")
        if con_or_new == "y":
            b = input("Enter the operation to be performed(+, -, *, /): ")
            if b == '+' or b == '-' or b == '*' or b == '/':
                c = float(input("Enter second number: "))
                d = cal[b](d, c)
                print(d)
            else:
                print("Enter a valid operation!!")
                continue

        elif con_or_new == "n":
            print("\n" * 50)
            print(art.logo)
            a = float(input("Enter first number: "))
            b = input("Enter the operation to be performed(+, -, *, /): ")
            c = float(input("Enter second number: "))
            d = cal[b](a, c)
            print(d)
        else:
            print("Invalid input")
            break
    elif y_or_n == "n":
        print("Thank you!")
        break
    else:
        print("Invalid input")
        break

