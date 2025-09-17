def executar_ciclo_lavagem(nome_do_ciclo, multiplicador):
  print(f"\n--- INICIANDO CICLO: {nome_do_ciclo.upper()} ---")
    
  iniciar = int(input("\nBaixo: 50L\nMédio: 125L\nAlto: 200L\nVoce deseja adicionar quantos Litros de Água? "))
  print("\nEspere a Máquina encher, ou tente novamente!\n")

  if iniciar <= 50:
    print (iniciar, "Litros foram colocados")
  elif iniciar <= 125:
    print (iniciar, "Litros foram colocados")
  elif iniciar <= 200:
    print(iniciar, "Litros foram adicionados")

  tempo_total = iniciar * multiplicador
        
  print(f"\nO timer de lavagem será de {tempo_total} segundos.")
        
  while True:
    tempo_total -= 1
    print(tempo_total, "segundos restantes...")
    if tempo_total <= 0:
      break
                
  print("\nA MÁQUINA ESTA CHEIA E O PRIMEIRO CICLO FOI CONCLUÍDO!!!")

print("!!Máquina de Lavar!!")
tipo = int(input("\n1: Pesada\n2: Leve\n3: Branca\nQual será o tipo de roupa: "))


if tipo == 1:
   executar_ciclo_lavagem("Lavagem Pesada", 1000) 
elif tipo == 2:
   executar_ciclo_lavagem("Lavagem Leve", 100)
elif tipo == 3:
   executar_ciclo_lavagem("Lavagem de Roupa Branca", 500)

adicionais = []

while True:
    adi = int(input("\n1: Sabão em pó \n2: Líquido para Limpeza \n3: Tira manchas \n4: Amaciante\n5: Ver Lista\n6: Nada\nO que deseja adicionar na Máquina:"))

    if adi == 1:
        adicionais.append("Sabão em Pó")
        print("\nSabão em pó foi Adicionado")
    elif adi == 2:
        adicionais.append("Líquido para Limpeza")
        print("\nLíquido para Limpeza foi Adicionado")
    elif adi == 3:
        adicionais.append("Tira Manchas")
        print("\nTira manchas foi Adicionado")
    elif adi == 4:
        adicionais.append("Amaciante")
        print("\nAmaciante foi Adicionado")
    elif adi == 5:
        print("\nSua lista de adicionais é:", adicionais)
    else:
        break

print("\nA MÁQUINA FOI INICIADA!!!")
contador = 100
if adi == 6:
    contador *= 100
    while True:
        contador -= 1
        print(contador, "segundos")
        if contador == 0:
            break

if contador == 0:
    cent = int(input("Deseja Ativar modo de Centrifuga?\n1: Sim\n2: Não\nDigite uma opção: "))
    if cent == 1:
        print("\nA MÁQUINA FOI INICIADA!!!")
contador = 100
contador *= 1000
while True:
    contador -= 1
    print(contador, "segundos")
    if contador == 0:
        break
print("A MÁQUINA ESTA PRONTA!!!")


