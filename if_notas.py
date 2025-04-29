nota = float(input("Qual foi sua nota? Digite apenas números: "))

if nota >= 7.0:
    print("Parabéns! Você foi aprovado.")
    print("Sua nota é:", nota)

elif 5.0 <= nota < 7.0:
    print("Você está de recuperação.")
    print("Sua nota é:", nota)
    print("Aumente sua nota em pelo menos 1.0 para ser aprovado.")

else:
    print("Você foi reprovado.")
    print("Sua nota é:", nota)

