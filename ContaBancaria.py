import random

class ContaBancaria:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado com sucesso na conta {self.numero}.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso na conta {self.numero}.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def exibir_saldo(self):
        print(f"Saldo da conta {self.numero}: {self.saldo}")
        return self.saldo

    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f"Transferência de {valor} realizada com sucesso da conta {self.numero} para a conta {conta_destino.numero}.")
        else:
            print("Saldo insuficiente ou valor de transferência inválido.")

    def to_dict(self):
        return {
            'numero': self.numero,
            'titular': self.titular,
            'saldo': self.saldo
        }

    @staticmethod
    def from_dict(d):
        conta = ContaBancaria(d['numero'], d['titular'])
        conta.saldo = d['saldo']
        return conta
