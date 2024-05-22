import json
from ContaBancaria import ContaBancaria

class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print(f"Conta {conta.numero} adicionada com sucesso.")

    def remover_conta(self, numero):
        conta = self.buscar_conta(numero)
        if conta:
            self.contas.remove(conta)
            print(f"Conta {numero} removida com sucesso.")
        else:
            print(f"Conta {numero} não encontrada.")

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

    def salvar_dados(self):
        dados = [conta.to_dict() for conta in self.contas]
        with open('dados_banco.json', 'w') as f:
            json.dump(dados, f)
        print("Dados salvos com sucesso.")

    def carregar_dados(self):
        try:
            with open('dados_banco.json', 'r') as f:
                dados = json.load(f)
                self.contas = [ContaBancaria.from_dict(d) for d in dados]
            print("Dados carregados com sucesso.")
        except FileNotFoundError:
            print("Nenhum dado encontrado.")
