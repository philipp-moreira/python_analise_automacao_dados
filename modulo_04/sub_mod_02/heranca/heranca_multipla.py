from dataclasses import dataclass


@dataclass(kw_only=True)
class Animal:
    """Classe base representativa de animais.

    Define atributos fisicos fundamentais e o formato de exibicao em string.
    """

    numero_patas: int

    def __str__(self) -> str:
        atributos = ", ".join([f"{k}: {v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}: {atributos}"


@dataclass(kw_only=True)
class Mamifero(Animal):
    cor_pelo: str


@dataclass(kw_only=True)
class Ave(Animal):
    cor_bico: str


@dataclass(kw_only=True)
class Cachorro(Mamifero):
    pass


@dataclass(kw_only=True)
class Gato(Mamifero):
    pass


@dataclass(kw_only=True)
class Leao(Mamifero):
    pass


@dataclass(kw_only=True)
class Ornitorrinco(Mamifero, Ave):
    """Representa a entidade Ornitorrinco (Heranca Multipla de Mamifero e Ave).

    Nota de Arquitetura:
    O uso do decorator @dataclass(kw_only=True) inspeciona recursivamente a hierarquia
    de classes e gera o metodo __init__ combinando todos os atributos esperados
    (numero_patas, cor_pelo, cor_bico). Isso resolve a opacidade de assinaturas
    gerada por **kwargs, garantindo autocompletar e validacao estatica no IDE.
    """

    pass


g1 = Gato(numero_patas=4, cor_pelo="marrom")
print(g1)

# Instanciacao com autocompletar 100% funcional no IDE
o1 = Ornitorrinco(numero_patas=4, cor_pelo="vermelho", cor_bico="marrom")
print(o1)
