class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print(f"{self.__class__.__name__}: Ligando motor . . .")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{k}: {v}' for k, v in self.__dict__.items()])}"


class Motocicleta(Veiculo): ...


class Carro(Veiculo): ...


class Caminhao(Veiculo):
    # OPCAO DE SOLUÇÃO 1:
    # Repasse de argumentos para construtor da super/pai classe
    # Observacao: Se o construtor da super classe mudar, tenho que fazer manutencao na  classe derivada/filha, para ajuste dos
    # parametros do construtor
    # def __init__(self, cor, placa, numero_rodas, carregado):
    #    super().__init__(cor, placa, numero_rodas)
    #    self.carregado = carregado

    # OPCAO DE SOLUÇÃO 2:
    # Repasse de argumentos para construtor da super/pai classe
    # Observacao: Mais flexivel e nao necessita de alteracao  na classe derivada, quando o construtor da super classe for alterado
    # permitindo a verdadeira mecanica do  conceito de POO (herança) ser "transparente"  para a(s) classe(s) derivada(s)
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.carregado = kwargs["carregado"]

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("Verde/Branca", "abc-123", 2)
print(moto)
moto.ligar_motor()

carro = Carro("Vermelho", "def-456", 4)
print(carro)
carro.ligar_motor()

caminhao = Caminhao("Branco", "ghi-890", 8, carregado=False)
print(caminhao)
caminhao.ligar_motor()
