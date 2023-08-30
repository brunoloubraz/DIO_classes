class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_do_pelo, **kw):
        self.cor_do_pelo = cor_do_pelo
        super().__init__(**kw)
    # def __str__(self):
    #     return self.__class__.__name__

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
    # def __str__(self):
    #     return 'ave 42'

class Gato(Mamifero):
    pass

class FalarMixin:
    def falar(self):
        return 'Oi, estou falando'

class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_do_pelo, nro_patas):
        # print(Ornitorrinco.__mro__)
        super().__init__(cor_do_pelo=cor_do_pelo, cor_bico=cor_bico, nro_patas=nro_patas)
    # def __str__(self):
    #     return 'Ornitorrinco'
    


gato = Gato(nro_patas=4, cor_do_pelo='Preto')
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_do_pelo='Vermelho', cor_bico='Laranja')
print(ornitorrinco)
print(ornitorrinco.falar())


class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())


class Bar(Foo):
    def hello(self):
        return super().hello()


bar = Bar()
bar.hello()
