class Pessoa:
    olhos: int = 5
    def __init__(self, *filhos, nome=None, age=34):
            self.nome = nome
            self.Idade = age
            self.filhos = list(filhos)

    def greets(this):
        return f"Oi {id(this)}"

if __name__=='__main__':
    Gow = Pessoa(nome='Gow') #Aqui a Fun Só recebeu Nome
    #Jogou como argumento um Objeto que contém uma Função.
    Dikson = Pessoa(Gow, nome='Dikson')#Aqui a Fun q só rec Nome é Adicionada no Arg Nome.
    #p = Pessoa('Gow') #Agora Posso Inserir nome aqui
    print(Pessoa.greets(Dikson))
    #Metodo Usual:
    print(Dikson.greets())
    print(id(Dikson))
    #Adicionamos Meu nome ao Atributo 'nome'
    #Dikson.nome = 'Dikson Santos' #Alterou Nome
    print(Dikson.nome)
    print(Dikson.Idade)
    for x in Dikson.filhos:
        print(Dikson.nome)

    #Criando Um Atributo PARA UM OBJETO, depois do __init__ ou no meio do Código:
    Dikson.sobrenome = 'Santos'
    print(Dikson.sobrenome)

    #O Objeto 'Gow' Não Possui o Atributo Sobrenome
    #Gow.sobrenome # Da Pau

    #Para Listar todos os Atrib de Cada Objeto:
    print(Dikson.__dict__)
    print(Gow.__dict__)

    #Removendo Atributo No meio Do codigo (Dinamicamente):
    del Dikson.sobrenome
    print("Sem Sobrenome Agora: ", Dikson.__dict__)

    print(Pessoa.olhos)
    print(Gow.olhos)
    print(id(Gow.olhos), "\n", id(Dikson.olhos),"\n" ,id(Pessoa.olhos))

    #Aqui ele não mostra 'Olhos' Como atributo. Pois ele esta antes do __init__
    print(Gow.__dict__)
#
    Gow.olhos = 3
    print(Gow.__dict__)

    #Agora o ID do objeto já é outro.
    print(id(Gow.olhos))

    #Para apagar A Alteração no caso 3 Olhos do Objeto e Não da Classe, usa-se DEL:
    del Gow.olhos
    #Agoras Ambos tem 3 olhos ->Gow esta herdando da Classe:
    print(Gow.olhos)
    print(Pessoa.olhos)

    #Agora Vamos mudar a Classe toda Para ter 3 Olhos:
    Pessoa.olhos = 3
    print("\n", id(Gow), "\n", id(Dikson), "\n", id(Pessoa))
    print(Pessoa.olhos)
