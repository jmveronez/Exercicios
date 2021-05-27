class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0
        self.__horas_trabalhadas = 0
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self,novo_salario):
        raise ValueError("Impossível alternar salário diretamente. Use a função calcula_salário().")

    @property
    def horas_trabalhadas(self):
        return self.__horas_trabalhadas
    
    @horas_trabalhadas.setter
    def horas_trabalhadas(self,new_hours):
        raise ValueError("Impossível alternar as horas diretamente. Use a função regista_hora_trabalhada().")

    def registra_hora_trabalhada(self, horas):
        self.__horas_trabalhadas += horas

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada

nome_func = input("Digite o nome do funcionário: ")
cargo_func = input("Digite o cargo do funcionário: ")
valor_hora = float(input("Qual o valor da sua hora de trabalho: "))
funcionario = Funcionario(nome_func,cargo_func,valor_hora)
horas = float(input("Digite o total de horas trabalhadas do funcionário: "))
funcionario.registra_hora_trabalhada(horas)
funcionario.calcula_salario()
print(f"Nome do Funcionário: {funcionario.nome}\nCargo do Funcionário: {funcionario.cargo}\nSalário atual: R${funcionario.salario}")