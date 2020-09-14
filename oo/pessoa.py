class Pessoa:
    def __init__(self, nome=None, age=34):
            self.nome = nome
            self.Idade = age

    def greets(this):
        return f"Oi {id(this)}"

if __name__=='__main__':
    p = Pessoa('Gow') #Agora Posso Inserir nome aqui
    print(Pessoa.greets(p))
    #Metodo Usual:
    print(p.greets())
    print(id(p))
    #Adicionamos Meu nome ao Atributo 'nome'
    p.nome = 'Dikson Santos'
    print(p.nome)
    print(p.Idade)



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
