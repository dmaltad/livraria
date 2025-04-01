class itemNaoEncontradoException(Exception):
    pass

class estoqueInsuficienteException(Exception):
    pass

class estoque:
    _itens = None


    def __init__(self, itens):
        self._itens = itens

    def processarVenda(self, titulo, quantidade):
        if titulo in self._itens:
            quantidadeEmEstoque = self._itens[titulo]["quantidade"]
            if quantidadeEmEstoque >= quantidade and quantidadeEmEstoque > 0:
                self._itens[titulo]["quantidade"] -= quantidade
                total = quantidade * self._itens[titulo]["livro"].preco
                return total
            else:
                raise estoqueInsuficienteException("Estoque insuficiente!")            
        else:
            raise itemNaoEncontradoException("Item não econtrado no estoque!")
    
class livro:
    _titulo = None
    _autor = None
    preco = None

    def __init__(self, titulo, autor, preco):
        self._titulo = titulo
        self._autor = autor
        self.preco = preco

estoque1 = estoque({"O senhor dos aneis":{"livro":livro("O senhor dos aneis", "J.R.R.Tokien", 60),"quantidade":30}})
print(estoque1.processarVenda("O senhor dos aneis", 3))
