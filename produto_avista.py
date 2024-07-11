produto = float(input('Qual eh o preço do produto? '))
vista = produto - (produto * 10/100)
prazo = produto + (produto * 10/100)
print(f'O valor do produto a vista com desconto fica: {vista} e o valor parcelado com acrescimo de 10% ficaria: {prazo}')