nota = float(input("Qual foi sua nota? Digite apenas números: "))

if nota >= 9.0 and nota <= 10:
    print("Excelente")
    print("Sua nota é:", nota)

elif nota >= 7.0 and nota <= 8.9:
    print("Bom")
    print("Sua nota é:", nota)

elif nota >= 5.0 and nota <= 6.9:
    print("Regular")
    print("Sua nota é:", nota)

elif nota <= 4.9:
    print("Reprovado")
    print("Sua nota é:", nota)

else:
    print("Nota inválida (fora do intervalo 0-10)")
