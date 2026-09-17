# Definicao
# As classes abaixo representam uma abstracao do contexto de objeto/aves que voam
# Como sao classes com correlacao do mundo real,  exemplificam que todas sabem como voar()
# mas, cada uma voa a sua maneira ou apenas re-utilizam o comportamento definido da super classe (pai)


class Passaro:
    def voar(self):
        print(f"{self.__class__.__name__}: Voando ...")


class Pardal(Passaro):
    def voar(self):
        super().voar()


class Avestruz(Passaro):
    """_summary_
    Nota(s):
    1 - Utilizado a classe aqui apenas para fins didáticos, pois no mundo real um Avestruz não voa.
    2 - Este exemplo feri um dos conceitos de SOLID, o "L", onde  o principio de substituição de liskov (LSP),
         define que todo objeto de uma dada hierarquia deve ser intercambiavel, ou seja, todo lugar da solução
         de código onde fosse definido que esta sendo feito o comportamento de voar(), deveria permitir que
         este comportamento fosse atendido,sempre, seja um objeto super (pai) ou uma das classes derivadas (filhas)
    """

    def voar(self):
        print(f"{self.__class__.__name__}: *Voando ...")


# Nesse momento vou caracterizar a função como sendo uma abstração do conceito de interface que vemos em
# outras tecnologias  onde o papel dele neste contexto é apenas demonstrar que é esperado  a passagem de um
# argumento/objeto que saiba como voar()
# Em python este conceito se define como Duck Typing
def plano_voo(obj):
    obj.voar()


# Uso
p1 = Passaro()
p2 = Pardal()
p3 = Avestruz()

plano_voo(p1)
plano_voo(p2)
plano_voo(p3)
