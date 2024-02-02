r = ""
for i in input():
    r += i.upper() if i.islower() else i.lower()
print(r)