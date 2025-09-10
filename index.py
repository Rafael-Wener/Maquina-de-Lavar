def maquina():
  print("Máquina de Lavar:")
  iniciar = int(input("\nBaixo: 50L\nMédio: 125L\nAlto: 200L\nVoce deseja adicionar quantos Litros de Água? "))
  print("\nEspere a Máquina encher, ou tente novamente!\n")
  if iniciar <= (50):
    print (iniciar, "Litros foram colocados")
  elif iniciar <= (125):
    print (iniciar, "Litros foram colocados")
  elif iniciar <= (200):
    print(iniciar, "Litros foram adicionados")
    iniciar *= 1000 

    while True:
        iniciar -= 1
        print(iniciar, "segundos")
        if iniciar == 0:
            break
    print("\nA MÁQUINA ESTA CHEIA!!!")
  else:
    maquina()
maquina()




while True:
  adi = int(input("\n1: Sabão em pó \n2: Líquido para Limpeza \n3: Tira manchas \n4: Amaciante\n5: Nada\nO que deseja adicionar na Máquina:"))

  if adi == 1:
    print("Sabão em pó foi Adicionado")
  elif adi == 2:
    print("Líquido para Limpeza foi Adicionado")
  elif adi == 3:
    print("Tira manchas foi Adicionado")
  elif adi == 4:
     print("\nAmaciante foi Adicionado")
  else:
   break
print("A MÁQUINA FOI INICIADA!!!")
