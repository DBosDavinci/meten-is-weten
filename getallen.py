a = int(input("geef een heel getal op"))
b = int(input("geef nog een heel getal op"))

if a > b:
    max = a
else:
    max = b
if a < b:    
    min = a
else:
    min = b

print("het minimum is:",min)
print("het maximum is:",max)