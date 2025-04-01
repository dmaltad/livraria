class itemNaoEncontradoException(Exception):
    print("Item não encontrado!")

class estoqueInsuficienteException(Exception):
    print("Estoque insuficiente!")

class estoque:
    _quantidade = None

    def __init__(self, quantidade):
        self._quantidade = quantidade

class livro(estoque):
    _titulo = None
    _autor = None
    _preco = None

    def __init__(self, titulo, autor, quantidade, preco):
        super().__init__(quantidade)
        self._titulo = titulo
        self._autor = autor
        self._preco = preco
        self._quantidade = quantidade

    def processarVenda(self, titulo, quantidade):
        if self._titulo == titulo:
            if self._quantidade >= quantidade and self._quantidade > 0:
                self._quantidade -= quantidade
                total = quantidade * self._preco
                return total
            else:
                print("Estoque insuficiente!")
        else:
            print("Item não encontrado!") 
        
livro1 = livro("O", "J.R.R.Tokien", 30, 60)
livro1.processarVenda("O", 2)
