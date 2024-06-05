
NOTA1 = float(input("Digite a nota 1: "))
NOTA2 = float(input("Digite a nota 2: "))
NOTA3 = float(input("Digite a nota 3: "))

MEDIA = (NOTA1 + NOTA2 + NOTA3) / 3

# VERIFICAR A MÉDIA
if MEDIA >= 7:
    print("O ALUNO ESTÁ APROVADO! MÉDIA DE {media:.2F}!")
elif MEDIA <= 5:
    print("O ALUNO ESTÁ EM RECUPERAÇÃO! MÉDIA DE {media:.2F}")
else:
    print("O ALUNO ESTÁ ARECPROVADO! MÉDIA DE {media:.2F}")
