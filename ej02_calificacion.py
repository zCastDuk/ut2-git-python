nota = int(input("Introduce la nota (0-10): "))

if nota >= 0 and nota < 5:
    calificación = 'Suspenso'
elif ndota >= 5 and nota < 7:
    calificación = 'Aprobades'
elif nota >=7 and nota < 9:
    calificación = 'Notable.'
elif nota >=9 and nota <=10:
    calificación = 'Sobresaliente.'
else: 
    calificación = 'No valido'
print(f"Calificación: {calificación}" )