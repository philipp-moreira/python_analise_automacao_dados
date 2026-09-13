class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{k}: {v}' for k, v in self.__dict__.items()])}"


# Ao  ter um cenário com heranca multipla:
# - Para que seja atendido o repasse de argumentos, para super classes(pai) sem a necessidade de ter quer incluir individualmente
# e eventualmente cada novo argumento da super classe no construtor da classe derivada (filha) o  uso de **kwargs (dict)
# se faz como o melhor "artificio"/tecnica; Tendo como trade-ff  apenas que todo consumidor desta hierarquia de classes,
# realize a criacao de instancia  usando a tecnica de argumentos nomeados
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo


class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)


class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass


class Leao(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave): ...


g1 = Gato(numero_patas=4, cor_pelo="marrom")
print(g1)

# Ao recorrer ao intellisense (documentacao  do objeto), ficou ilegivel  quais são os argumentos esperados
o1 = Ornitorrinco(numero_patas=4, cor_pelo="vermelho", cor_bico="marro")
print(o1)
