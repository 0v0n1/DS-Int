person = ["Avani", 21, "Engineer", "Lucknow", "India", "Single", "avani@example"]
print(f"Name: {person[0]}")
print(f"Age: {person[1]}")
print(f"Occupation: {person[2]}")
print(f"City: {person[3]}")
print(f"Country: {person[4]}")
print(f"Marital Status: {person[5]}")
print(f"Email: {person[6]}")

for i, value in enumerate(person):
    print(f"Index {i}: {value}")