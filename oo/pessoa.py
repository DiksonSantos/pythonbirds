class Pessoa:

    def greets(this):
        return f"Oi {id(this)}"

if __name__=='__main__':
    p = Pessoa()
    print(Pessoa.greets(p))
    #Metodo Usual:
    print(p.greets())

    print(id(p))

    #Obs:
    #print(p.greets(7))
    #Seria o mesmo que:
    #print(Pessoa.greets(p,7))
    #Isto a Cima seria o mesmo que estar passando 2 argumentos
    #..a FUN só suporta 1.

#Alteration
