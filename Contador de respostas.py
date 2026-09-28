# Contadores das respostas
qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

# Pesquisa com 10 entrevistados
for i in range(1, 11):

    print(f"\n--- Entrevistado {i} de 10 ---")

    # Entrada dos dados
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("\nOpinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião (1, 2 ou 3): "))

    # Contabilização das respostas
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 2:
        qtd_bom += 1
    elif opiniao == 3:
        qtd_ruim += 1
    else:
        print("Opção inválida!")

# Exibição dos resultados
print("\n========== RESULTADO DA PESQUISA ==========")
print(f"EXCELENTE: {qtd_excelente}")
print(f"BOM:       {qtd_bom}")
print(f"RUIM:      {qtd_ruim}")