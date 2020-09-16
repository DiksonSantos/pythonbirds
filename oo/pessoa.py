class Pessoa:
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



#


"""
class Pessoa:
    def __init__(self):
            self.nome = None

    def greets(this):
        return f"Oi {id(this)}"

if __name__=='__main__':
    p = Pessoa()
    print(Pessoa.greets(p))
    #Metodo Usual:
    print(p.greets())
    print(id(p))
    #Adicionamos Meu nome ao Atributo 'nome'
    p.nome = 'Dikson'
    print(p.nome)
"""




    #Obs:
    #print(p.greets(7))
    #Seria o mesmo que:
    #print(Pessoa.greets(p,7))
    #Isto a Cima seria o mesmo que estar passando 2 argumentos
    #..a FUN só suporta 1.

#Alteration
