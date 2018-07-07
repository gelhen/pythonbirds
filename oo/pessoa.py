class Pessoa:
    def __init__(self, nome=None, idade=35): # metodo executado quanto constroi o objeto
        self.idade = idade
        self.nome  = nome #atributo de dados

    def cumprimentar(self):  #atributo de metodo
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'André'
    print(p.nome)
    print(p.idade)