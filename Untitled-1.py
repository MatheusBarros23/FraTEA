
print(f"\n======FRASE======\n| 1 -\t{}\t|\n| 2 -\tCOMEU\t|\n| 3 -\tFEIJÃO\t|\n=================")
print(f"\t\  /\n\t \/\t\t\n")
print(f"===CORRELAÇÃO====\n| SUJEITO  - 1\t|\n| VERBO\t   - 2\t|\n| OBJETO   - 3\t|\n=================")

opcaoF=int(input("\nQUAL ELEMENTO DA FRASE DESEJA TRABALHAR: "))
opcaoC=int(input("\nQUAL O CAMPO DA FRASE ELE PERTENCE: "))

if opcaoC == opcaoF:
  print("\n!!! ACERTOU !!!\n")
else:
  print("\n!!! ERROU D: !!!\n")
