# Tarefa 03 - Lógica de programação
# Seu nome Aqui: Luam Ahrion


lista_produtos = ['1001', '1324', '6548', '2987', '7623']
lista_precos =   [ 5.32 ,  6.45 ,  2.37 ,  5.32 ,  6.45 ]
lista_prod = []
lista_qtd = []
lista_sub = []

nome = input("Nome do Cliente: ")

while True:

    codigo = input("[fim - finaliza] - Código do Produto: ") ###CODIGO
    if codigo == 'fim':
            break

    if codigo not in lista_produtos:
        input("Código Inválido")
        continue

    while True:

        try:

            quantidade = int(input(f"Quantidade do produto {codigo}: ")) ###QUANTIDADE
            if quantidade <= 0:
                input("Quantidade deve ser maior que 0")
                continue
            break

        except:

            input("Quantidade Inválida")
            continue

    for x, cod in enumerate(lista_produtos):
        if codigo == cod:
            lista_prod.append(codigo)
            lista_qtd.append(quantidade)
            lista_sub.append(quantidade*lista_precos[x])

total = sum(lista_sub)

print('''
======================================
''')
        
print("Cliente: ",nome)
print()
print("Prod - Qtd - Subtotal")
print()

for x in range (len(lista_prod)):

    print(f"{lista_prod[x]} -  {lista_qtd[x]}  - {lista_sub[x]}")

print()
print(f"Total: ",total)

print('''
======================================
''')

input()
