try:
    num= float(input("1st number: "))
    den= float(input("2nd number: "))

    result= num/den
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: can not divide by zero")
except ValueError:
    print("Error: enter valid numbers only")