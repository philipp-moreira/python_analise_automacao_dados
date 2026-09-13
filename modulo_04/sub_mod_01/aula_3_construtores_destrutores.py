class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim plim. . . ")

    def parar(self):
        print("Bicicleta parando....")
        print("Bicicleta parada!")

    def correr(self):
        print("Bicicleta correndo...")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{k}: {v}' for k, v in self.__dict__.items()])}"


b1 = Bicicleta("amarela", "caloi", 2026, 650.78)
# forma 1
b1.correr()
b1.buzinar()
b1.parar()

print(b1)

b2 = Bicicleta("roxa", "monark", 2003, 250.00)
Bicicleta.buzinar(b2)
