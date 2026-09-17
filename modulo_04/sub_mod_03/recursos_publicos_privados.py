class Pessoa:
    def __init__(self, nome, ano_nascimento, documento):
        # Atributos internos da classe sao prefixados com "_" (1 underline) para indicar encapsulamento por "convencao"
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        self._documento = documento

    @property  # Já define o atributo como tendo um getter
    def nome(self):
        return self._nome

    @nome.setter  # Define que o  atributo interno pode ser alterado
    def nome(self, nome_alterado):
        # Exemplo que como um atributo ao ser encapsulado, pode ter uma lógica de consistência interna
        # para mitigar erro de uso/alteracao
        if not self.__valida_nome(nome_alterado):
            return
        self._nome = nome_alterado

    @nome.deleter
    def nome(self):
        self._nome = (
            f"{''.join([self.__ocultar_dado(char) for char in str(self.nome)])}"
        )
        print("\tNome ocultado por questões de proteção  de dados.")

    @property
    def documento(self):
        return self._documento

    @documento.deleter
    def documento(self):
        self._documento = (
            f"{''.join([self.__ocultar_dado(char) for char in self.documento])}"
        )

    def __valida_nome(self, nome_alterado) -> bool:
        if len(str.strip(nome_alterado)) < 1:
            print(
                f"\tO novo valor de nome '{nome_alterado}' é inválido e pode gerar divergencias.\t|\tAlteração não realizada."
            )
            return False
        return True

    def __ocultar_dado(self, value) -> chr:
        lower_character = "x"
        upper_character = "X"
        result = value

        if value.isalpha():
            if value.isupper():
                result = upper_character

            else:
                result = lower_character

        elif value.isdigit():
            result = lower_character

        else:
            result = value

        return result

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'\t{k}: {v}' for k, v in self.__dict__.items()])}"


p1 = Pessoa("Jhonn Doe", 1997, "123456-789")
print(p1)
p1.nome = ""
print(p1)
print(p1.nome)

# Emulando uma necessidade de proteção de dado para LGPD
# Onde os dados sensiveis da pessoa são ocultados,  para repasse/log do objeto
# sem exposição de dados sensiveis
del p1.nome
print(p1)

del p1.documento
print(p1)
