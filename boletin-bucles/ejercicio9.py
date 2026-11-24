f = input ("¿Cuántas notas?: ")
n = 0
for f in range(1, int(f) + 1):
    nota = float(input("Nota " + str(f) + ": "))
    media = nota / int(f)
print ("Nota media:" ,media)