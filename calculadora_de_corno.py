import random

# Banco de dados com os nomes
nomes_femininos = [
    "Helena", "Alice", "Laura", "Maria Alice", "Cecília", "Maitê", "Liz", "Aurora", "Antonella", "Heloísa",
    "Maria Cecília", "Maria Clara", "Manuela", "Maya", "Sophia", "Valentina", "Elisa", "Maria Helena", "Isabella",
    "Eloá", "Ayla", "Lara", "Lívia", "Maria Júlia", "Lorena", "Melissa", "Sofia", "Isabela", "Luísa", "Beatriz",
    "Júlia", "Mariana", "Isadora", "Maria Luiza", "Ana Liz", "Rebeca", "Isis", "Maria Eduarda", "Aylla", "Esther",
    "Manuella", "Sarah", "Ísis", "Maria Liz", "Olívia", "Lavínia", "Ana Laura", "Catarina", "Maria", "Luna",
    "Ana Clara", "Luiza", "Yasmin", "Marina", "Emanuelly", "Giovanna", "Jade", "Eloah", "Julia", "Clara",
    "Maria Luísa", "Ana Júlia", "Ester", "Anna Liz", "Agatha", "Stella", "Alícia", "Gabriela", "Maria Laura",
    "Sara", "Maria Flor", "Heloisa", "Hellena", "Clarice", "Maria Isis", "Bella", "Isabelly", "Melina", "Mirella",
    "Rafaela", "Vitória", "Maria Julia", "Cecilia", "Allana", "Olivia", "Alana", "Zoe", "Mariah", "Ana Luiza",
    "Lunna", "Bianca", "Hadassa", "Maria Vitória", "Maria Fernanda", "Luara", "Milena", "Ágatha", "Laís",
    "Ana Cecília", "Ana Beatriz"
]

nomes_masculinos = [
    "Miguel", "Heitor", "Gael", "Arthur", "Bernardo", "Davi", "Ravi", "Noah", "Samuel", "Théo",
    "Gabriel", "Anthony", "Pedro", "Benício", "Joaquim", "Isaac", "Lorenzo", "João Miguel", "Lucas", "Levi",
    "Henrique", "Rafael", "Henry", "Theo", "Nicolas", "Murilo", "Guilherme", "Benjamin", "Lucca", "Matheus",
    "Matteo", "Pedro Henrique", "Bento", "Gustavo", "Leonardo", "Vicente", "Daniel", "João Pedro", "Emanuel",
    "Pietro", "Davi Lucca", "Bryan", "Felipe", "Enzo Gabriel", "Antony", "Mateus", "Anthony Gabriel", "João Lucas",
    "Augusto", "João Guilherme", "Benjamim", "Thomas", "João", "Eduardo", "Antônio", "Yuri", "Enzo", "Oliver",
    "Rael", "Otávio", "Francisco", "Rhavi", "João Gabriel", "Nathan", "Mathias", "Caio", "Arthur Miguel", "Brayan",
    "Isaque", "José", "Ryan", "Ravi Lucca", "Enrico", "Davi Lucas", "Josué", "Benicio", "José Miguel", "Luan",
    "Luiz Miguel", "Ravy", "Vinícius", "Apollo", "Otto", "Theodoro", "Yan", "Dom", "Pedro Lucas", "Léo",
    "Davi Miguel", "Valentim", "Caleb", "José Pedro", "Liam", "Dante", "Gael Henrique", "Henry Gabriel", "Kevin",
    "Arthur Gabriel", "Asafe", "Erick"
]

def simular_traicao():
    # Simulação de % de traição
    porcentagem_traicao = random.randint(0, 100)
    return porcentagem_traicao

def adivinhar_nome_primeira_letra(letra_primeira, genero):
    if genero == 'f':
        nomes = nomes_femininos
    elif genero == 'm':
        nomes = nomes_masculinos
    else:
        print("Gênero inválido.")
        return

    # Filtrar nomes que começam com a letra conhecida
    possiveis_nomes = [nome for nome in nomes if nome.lower().startswith(letra_primeira)]

    if possiveis_nomes:
        if len(possiveis_nomes) == 1:
            print("O nome mais provável é:", possiveis_nomes[0])
        else:
            print("Mais de um nome começa com essa letra. Vamos tentar descobrir mais?")
            letra_ultima = input("Qual é a última letra do nome? ").lower()
            possiveis_nomes = [nome for nome in possiveis_nomes if nome.lower().endswith(letra_ultima)]
            if possiveis_nomes:
                print("O nome mais provável é:", possiveis_nomes[0])
            else:
                print("Não foi possível determinar o nome.")

        # Simulação de traição
        porcentagem = simular_traicao()
        print("A probabilidade de estar sendo traído(a) é de {}%.".format(porcentagem))
    else:
        print("Não foi possível encontrar nomes que comecem com a letra fornecida.")

# Pedir ao usuário para fornecer a primeira letra do nome e o gênero
letra = input("Digite a primeira letra do nome: ").lower()
genero = input("Digite o gênero (f para feminino, m para masculino): ").lower()

# Chamar a função para adivinhar o nome a partir da primeira letra e do gênero
adivinhar_nome_primeira_letra(letra, genero)
