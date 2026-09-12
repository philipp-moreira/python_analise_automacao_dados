# lista vazia
frutas = []
print(f"frutas \t\t\t=> {frutas}")

# lista preenchida
frutas_preenchida = ["laranja", "maca", "uva"]
print(f"frutas_preenchida \t=> {frutas_preenchida}")

# String é um objeto interavel,  ou seja, a string "não é interpretada" como um único valor, mas, como um "conjunto de letras"
# Usando o construtor do tipo List, se cria uma lista a partir de um interavel"
letras_python = list("Python")
print(f"letras_python \t\t=> {letras_python}")

print(f"\tAcessando o primeiro elemento: {letras_python[0]}")
print(f"\tAcessando o último  elemento: {letras_python[-1]}")
print(f"\tAcessando uma fatia/slice: {letras_python[2:4:1]}")

# Quase a mesma abordagem acima, mas, aqui é construído/convertido a partir de um range
# O range esta especificando para iniciar em 10 (start),  para  em 21 (não inclusivo - stop), utilizando o incremento de
# 1 em 1 (step)
numeros = list(range(10, 21, 1))
print(f"numeros \t\t=> {numeros}")

numeros_Ao_quadrado = [numero**2 for numero in numeros]
print(f"numeros_Ao_quadrado \t=> {numeros_Ao_quadrado}")

numeros_par_ao_quadrado = [numero**2 for numero in numeros if numero % 2 == 0]
print(f"numeros_par_ao_quadrado => {numeros_par_ao_quadrado}")


# Pseudo-objeto (meu entendimento)
# Demonstrado que a lista pode trazer elementos de tipos de dados diferentes
# e esta mecanica, demonstra a emulação do que um objto abstrai/representa
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(f"carro \t\t\t=> {carro}")

# O loop/laço "for" em python é análogo ao "for each" de outras linguagens/tecnologias
# Usando o operador de associação "in" é possível recuperar cada elemento do interavel
for caracteristica in carro:
    print(f"\t\t\t\tCaracteristica de carro: {caracteristica}")

matriz = [frutas, frutas_preenchida, letras_python, numeros, carro]
print(f"matriz \t\t\t=> {matriz}")

# Para se emular o loop/laço  for visto em outras tecnologias, podemos usar a classe enumerate
# ela "encapsula" o comportamento de criar um índice/contador ao percorrer e retornar o
# índice/contador + a referência/cópia do objeto do interavel
for indice, item in enumerate(matriz):
    print(f"\t\t\t\tElemento ({indice})\t-\tValor: {item}")
