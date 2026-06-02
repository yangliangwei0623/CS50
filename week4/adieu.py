import inflect
names = []
while True:
    name = input("Name: ")
    if not name:
        break
    names.append(name)
p = inflect.engine()
print(f"Adieu, adieu, to {p.join(names)}")