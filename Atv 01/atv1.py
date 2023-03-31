rodas = input("Olá. Vamos indicar qual melhor habilitação pra vc! Qual a quantidade de rodas tem seu carro?")
pessoas = float(input("Qual a quantidade máxima de pessoas cabe no seu veículo?"))
peso = float (input("Qual o peso do seu veículo?"))

if (rodas<=3):
    print("Habilitação tipo A é a indicada!")

elif (rodas==4 and peso<=3500 and pessoas<=8):
    print("Habilitação tipo B é a indicada!")

elif(rodas>=4 and 3500<peso and peso<6000):
    print("Habilitação tipo C é a indicada!")

elif(rodas>=4 and pessoas>8):
    print("Habilitação tipo D é a indicada!")

elif(rodas>=4 and peso<6000):
    print("Habilitação tipo E é a indicada!")

