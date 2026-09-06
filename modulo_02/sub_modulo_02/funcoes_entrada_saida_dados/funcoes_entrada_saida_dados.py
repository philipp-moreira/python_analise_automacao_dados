# Capta valor na mesma linha da label/mensagem para usuário
# name = input("Informe um nome:")
# age = input("Informe a idade:")

# Capta valor em uma  linha diferente da label/mensagem para usuário
name = input("Informe um nome:\n")
age = input("Informe a idade:\n")


# Exibe a mensagem na saida padrão (Console/Terminal)

print(f"{name} tem {age} anos")

print(f"{name} tem {age} anos", end=". . .\n\n")

print(name, age, sep="|", end=" <<<")
