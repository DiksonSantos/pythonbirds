class Pessoa:
    olhos: int = 5
    def __init__(self, *filhos, nome=None, age=34):
            self.nome = nome
            self.Idade = age
            self.filhos = list(filhos)

    def greets(this):
        return f"Oi, meu nome é: {this.nome}"


    @classmethod
    def nome_e_atributos_de_classe(cls):
        '''Permite Acessar os Metodos da CLasse Pessoa'''
        return f'{cls} - olhos {cls.olhos}'

    @staticmethod
    def metodo_estatico(self):
        return 10+10


class Homem(Pessoa):
    def greets(this):
        #cumprimentar_da_classe = Pessoa.greets(this)
        #OUTRA FORMA DE FAZER EXATAMENTE O QUE A LINHA DE CIMA FAZ (PORÉM
        #..USANDO O SUPER().DEF_desejada
        cumprimentar_da_classe = super().greets()
        return f'{cumprimentar_da_classe}:  Aperto de Mão'


class Mutante(Pessoa):
    '''Simples -> Sobrescrever os valores dos metodos da classe pai :/'''
    olhos = 3



if __name__=='__main__':

    #Classe Homem Herdou de Pessoa, assim substitui 'Pessoa' por 'Homem' e Funciona tbm:
    #Gow = Homem(nome='Gow') #Aqui a Fun Só recebeu Nome
    #print(Gow)
    Gow = Mutante('', 'GowDikson', 34)

    #Gow = Pessoa(nome='Gow') #Aqui a Fun Só recebeu Nome
    #Jogou como argumento um Objeto que contém uma Função.
    Dikson = Pessoa(Gow, nome='Dikson')#Aqui a Fun q só rec Nome é Adicionada no Arg Nome.
    print(Dikson.greets()) #Aqui é Da Classe Original\Pai
    #p = Pessoa('Gow') #Agora Posso Inserir nome aqui
    #print(Pessoa.greets(Dikson))
    #Metodo Usual:
    Dsantos = Homem(Gow, nome='Eu_Mesmo')
    print(Dsantos.greets())# Aqui vem da Classe 'Homem'

    #print(id(Dikson))
    #Adicionamos Meu nome ao Atributo 'nome'
    #Dikson.nome = 'Dikson Santos' #Alterou Nome
    #print(Dikson.nome)
    #print(Dikson.Idade)
    #for x in Dikson.filhos:
        #print(Dikson.nome, 'Linha do FOR')

    #Criando Um Atributo PARA UM OBJETO, depois do __init__ ou no meio do Código:

    Dikson.sobrenome = 'Santos'    #ACABOU DE SER CRIADO AQUI O ATRIB sobrenome.
    #print(Dikson.sobrenome)

    #O Objeto 'Gow' Não Possui o Atributo Sobrenome
    #Gow.sobrenome # Da Pau

    #Para Listar todos os Atrib de Cada Objeto:
    #print(Dikson.__dict__)
    #print(Gow.__dict__)

    #Removendo Atributo No meio Do codigo (Dinamicamente):
    del Dikson.sobrenome
    #print("Sem Sobrenome Agora: ", Dikson.__dict__)

    print('Atributo Original da Classe PAI: ', Pessoa.olhos, 'Olhos')
    print('Obj Gow da Classe Mutante Tem: ', Gow.olhos, ' Olhos')
    #print(id(Gow.olhos), "\n", id(Dikson.olhos),"\n" ,id(Pessoa.olhos))

    #Aqui ele não mostra 'Olhos' Como atributo. Pois ele esta antes do __init__
    #print(Gow.__dict__)
#
    #Gow.olhos = 3
    #print(Gow.__dict__)

    #Agora o ID do objeto já é outro.
    #print(id(Gow.olhos))

    #Para apagar A Alteração no caso 3 Olhos do Objeto e Não da Classe, usa-se DEL:
    #del Gow.olhos
    #Agoras Ambos tem 3 olhos ->Gow esta herdando da Classe:
    #print(Gow.olhos)
    #print(Pessoa.olhos)

    #Agora Vamos mudar a Classe toda Para ter 4 Olhos:
    Pessoa.olhos = 4
    #print("\n", id(Gow), "\n", id(Dikson), "\n", id(Pessoa))
    #print(Pessoa.olhos)

#@Classmethod
X = Pessoa.nome_e_atributos_de_classe()
#print(X, "DECORATOR")

#StaticMethod
J = Pessoa.metodo_estatico(10)
#print(J)
"""
print(Dikson.nome_e_atributos_de_classe())
print(Dikson.nome)

print(isinstance(Dikson, Pessoa)) #Dikson pertence á classe Pessoa ? True
print(isinstance(Homem, Pessoa)) #False Homem Não Pertence á Pessoa
print(isinstance(Pessoa, Homem)) #False
print(isinstance(Dikson, Homem)) #Não Pertence Ou Não esta associado á ...
print(isinstance(Gow, Homem)) #Sim True
"""

#print(Dikson.olhos)
#print(Homem.olhos) #Classe Homem Herda Olhos de Pessoa
#print(Gow.olhos)
