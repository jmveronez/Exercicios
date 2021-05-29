class Pessoa:
    def __init__(self,nome,idade,cpf,telefone):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__telefone = telefone

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def getCPF(self):
        return self.__cpf

    def getTelefone(self):
        return self.__telefone

    def setNome(self,nome):
        self.__nome = nome

    def setIdade(self,idade):
        self.__idade = idade

    def setCPF(self,cpf):
        senha = input("Digite a senha para alterar o CPF: ")
        if senha == "12345":
            self.__cpf  = cpf
            print("CPF alterado!")
        else:
            print("Senha Incorreta!")
    
    def setTelefone(self,telefone):
        self.__telefone = telefone

class Advogado(Pessoa):
    def __init__(self, nome, idade, cpf, telefone,oab):
        super().__init__(nome, idade, cpf, telefone)
        self.__oab = oab
    
    def getOAB(self):
        return self.__oab

class Medico(Pessoa):
    def __init__(self, nome, idade, cpf, telefone,crm):
        super().__init__(nome, idade, cpf, telefone)
        self.__crm = crm
    
    def getCRM(self):
        return self.__crm

medico = Medico("Jonas",25,"12345678-9","16 98134 9565","OK")
advogado = Advogado("Tulio",35,"9876532-1","16 9856 6595","Cassada")

print(medico.getCRM())
print(advogado.getOAB())