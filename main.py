import random
from Banco import Banco
from ContaBancaria import ContaBancaria

def gerar_numero_conta():
    return str(random.randint(1000, 9999))

if __name__ == "__main__":
    banco = Banco()
    banco.carregar_dados()

    conta_usuario = None

    while True:
        while not conta_usuario:
            print("\nVocê já tem uma conta bancária?")
            print("1. Sim")
            print("2. Não")
            opcao_inicial = input("Escolha uma opção: ")

            if opcao_inicial == '1':
                numero = input("Número da sua conta: ")
                conta_usuario = banco.buscar_conta(numero)
                if conta_usuario:
                    print(f"Conta {numero} encontrada, {titular}.")
                else:
                    print("Conta não encontrada. Tente novamente.")
            elif opcao_inicial == '2':
                titular = input("Nome do titular: ")
                numero = gerar_numero_conta()
                conta_usuario = ContaBancaria(numero, titular)
                banco.adicionar_conta(conta_usuario)
                print(f"Conta criada com sucesso. Seu número de conta é {numero}.")
            else:
                print("Opção inválida. Tente novamente.")

        while conta_usuario:
            print("\nOpções:")
            print("1. Realizar depósito")
            print("2. Realizar saque")
            print("3. Realizar transferência")
            print("4. Exibir saldo")
            print("5. Mudar de conta")
            print("6. Salvar e sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                valor = float(input("Valor do depósito: "))
                conta_usuario.depositar(valor)
            elif opcao == '2':
                valor = float(input("Valor do saque: "))
                conta_usuario.sacar(valor)
            elif opcao == '3':
                numero_destino = input("Número da conta de destino: ")
                valor = float(input("Valor da transferência: "))
                conta_destino = banco.buscar_conta(numero_destino)
                if conta_destino:
                    conta_usuario.transferir(valor, conta_destino)
                else:
                    print("Conta de destino não encontrada.")
            elif opcao == '4':
                conta_usuario.exibir_saldo()
            elif opcao == '5':
                conta_usuario = None
            elif opcao == '6':
                banco.salvar_dados()
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

        if opcao == '6':
            break
