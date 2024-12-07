Namen = ["Martin", "Basti", "Marie", "Andi"]
mx = ["Audi", "BMW"]
print(Namen)
Namen.sort()
print("sortiert")
print(Namen)

Namen.reverse()
print("reverse")
print(Namen)

# neu_name = input ("Neuer Name? ")
# Namen.append(neu_name)

print("Hinzugefügt")
print(Namen)

Namen.insert(1, 1000)
print(Namen)

Namen.insert(1, mx)

print(Namen)
print()

for einzelwert in Namen:
    print(einzelwert)
    print(type(einzelwert))

print("nach der for-Schleife")
