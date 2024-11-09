import json
from Produto import Produto

class Venda:
    def __init__(self, dataVenda):
        self.__produtos = []
        self.__dataVenda = dataVenda
        self.__total = 0.0

    def get_produtos(self):
        return self.__produtos
        
    def get_dataVenda(self):
        return self.__dataVenda

    def get_total(self):
        return self.__total

    def set_dataVenda(self, dataVenda):
        self.__dataVenda = dataVenda

    def calcularTotal(self):
        total = 0.0
        for produto in self.__produtos:
            total += produto.get_preco() * produto.get_quantidade()
        self.__total = total
        return total

    def removerProduto(self, nome):
        for produto in self.__produtos:
            if produto.get_nome() == nome:
                self.__produtos.remove(produto)
                print(f"Produto {nome} removido.")
                return
        print(f"Produto {nome} não encontrado.")

    def listarProdutos(self):
        if not self.__produtos:
            print("Nenhum produto na venda.")
        else:
            print(f"\nProdutos na Venda do dia {self.__dataVenda}:")
            for produto in self.__produtos:
                print(f"Nome: {produto.get_nome()}, Preço: R${produto.get_preco():.2f}, Quantidade: {produto.get_quantidade()}")
            print(f"Total da Venda: R${self.calcularTotal():.2f}")

    def salvarVenda(self):
        venda_data = {
            'dataVenda': self.__dataVenda,
            'produtos': [
                {
                    'nome': produto.get_nome(),
                    'preco': produto.get_preco(),
                    'quantidade': produto.get_quantidade()
                }
                for produto in self.__produtos
            ],
            'total': self.__total
        }
        try:
            with open('vendas.json', 'a') as f:
                json.dump(venda_data, f, ensure_ascii=False, indent=4)
                f.write("\n")
            print("Venda salva com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar a venda: {e}")

    @staticmethod
    def carregarVendas():
        try:
            vendas = []
            with open('vendas.json', 'r') as f:
                for line in f:
                    vendas.append(json.loads(line))  # Carregar cada venda salva
            return vendas
        except FileNotFoundError:
            print("Arquivo de vendas não encontrado.")
            return []
        except Exception as e:
            print(f"Erro ao carregar as vendas: {e}")
            return []
