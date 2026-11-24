f = input ("¿Cuántas notas?: ")
n = 0
for f in range(1, int(n) + 1):
    nota = float(input("Nota " + str(f) + ": "))
    media = nota / int(n)
print ("Nota media:" ,media)
if str (f) > "5":
    print ("Aprobado")
if str (f) < "5":
    print ("Suspenso")