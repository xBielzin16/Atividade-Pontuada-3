import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Reserva:
    pass

avioes = [None] * 4
assentos = [0] * 4
reservas = []

def registrar_avioes():
    for i in range(4):
        avioes[i] = input(f"Informe o número do avião {i+1}: ")

def registrar_assentos():
    for i in range(4):
        if avioes[i] is None:
            print("Primeiro registre os aviões (Opção 1).")
            return
        assentos[i] = int(input(f"Informe a quantidade de assentos disponíveis para o avião {avioes[i]}: "))

def reservar_passagem():
    if len(reservas) >= 20:
        print("Limite máximo de 20 reservas atingido!")
        return
    numero_aviao = input("Informe o número do avião: ")
    if numero_aviao not in avioes:
        print("Este avião não existe!")
        return
    indice = avioes.index(numero_aviao)
    if assentos[indice] <= 0:
        print("Não há assentos disponíveis para este avião!")
        return
    nome_passageiro = input("Informe o nome do passageiro: ")
    r = Reserva()
    r.numero_aviao = numero_aviao
    r.nome_passageiro = nome_passageiro
    reservas.append(r)
    assentos[indice] -= 1
    print("Reserva realizada com sucesso!")

def consulta_por_aviao():
    numero_aviao = input("Informe o número do avião: ")
    if numero_aviao not in avioes:
        print("Este avião não existe!")
        return
    reservas_aviao = [r for r in reservas if r.numero_aviao == numero_aviao]
    if not reservas_aviao:
        print("Não há reservas realizadas para este avião!")
    else:
        print(f"Reservas para o avião {numero_aviao}:")
        for r in reservas_aviao:
            print(f"- Passageiro: {r.nome_passageiro}")

def consulta_por_passageiro():
    nome_passageiro = input("Informe o nome do passageiro: ")
    reservas_passageiro = [r for r in reservas if r.nome_passageiro.lower() == nome_passageiro.lower()]
    if not reservas_passageiro:
        print("Não há reservas realizadas para este passageiro!")
    else:
        print(f"Reservas para o passageiro {nome_passageiro}:")
        for r in reservas_passageiro:
            print(f"- Avião: {r.numero_aviao}")

def menu():
    while True:
        print("\n--- Sistema de Gestão de Reservas - Sweet Flight ---")
        print("1. Registrar número dos aviões")
        print("2. Registrar assentos disponíveis")
        print("3. Reservar passagem aérea")
        print("4. Consulta por avião")
        print("5. Consulta por passageiro")
        print("6. Fechar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            registrar_avioes()
        elif opcao == "2":
            registrar_assentos()
        elif opcao == "3":
            reservar_passagem()
        elif opcao == "4":
            consulta_por_aviao()
        elif opcao == "5":
            consulta_por_passageiro()
        elif opcao == "6":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")

menu()