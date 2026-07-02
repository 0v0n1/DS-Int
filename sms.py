F = "student.txt"

class Student:
    def __init__(self, r, n, a, c):
        self.r, self.n, self.a, self.c = r, n, a, c

    def __str__(self):
        return f"{self.r},{self.n},{self.a},{self.c}"


def add():
    s=Student(input("Roll: "), input("Name: "), input("Age: "), input("Course: "))
    with open(F, "a") as f:
        f.write(str(s), "\n")

def view():
    try:
        with open(F, "r") as f:
            for i in f:
                print(i.strip().replace(",", "|"))
    except FileNotFoundError:
        print("File not found")


def search():
    r = input("Enter Roll: ")
    try:
        with open(F, "r") as f:
            for i in f:
                if i.startswith(r + ","):
                    print(i.strip())
                    return
            print("Not Found")
    except FileNotFoundError:
        print("File not found")


def update():
    r = input("Enter Roll: ")
    try:
        with open(F, "r") as f:
            data = f.readlines()

        with open(F, "w") as f:
            for i in data:
                if i.startswith(r + ","):
                    s = Student(r, input("Name: "), input("Age: "), input("Course: "))
                    f.write(str(s) + "\n")
                else:
                    f.write(i)
    except FileNotFoundError:
        print("File not found")


def delete():
    r = input("Enter Roll: ")
    try:
        with open(F, "r") as f:
            data = f.readlines()

        with open(F, "w") as f:
            for i in data:
                if not i.startswith(r + ","):
                    f.write(i)
    except FileNotFoundError:
        print("File not found")


while True:
    print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
    ch = input("Choice: ")

    match ch:
        case "1": add()
        case "2": view()
        case "3": search()
        case "4": update()
        case "5": delete()
        case "6": break
        case _: print("Invalid Choice")