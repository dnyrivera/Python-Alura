1 -

# Coletar os números
num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))

# Comparamos ambos os números e descobrimos qual é o maior
if num1 > num2:
    print(f'O primeiro número é maior: {num1}')
elif num2 > num1:
    print(f'O segundo número é maior: {num2}')
else: # Caso os números sejam iguais
    print('Os dois números são iguais.')
Copiar código
2 -

# Coleta do percentual
variacao = float(input('Digite o percentual de crescimento: '))

# Verifica se o valor é positivo ou negativo com uma verificação se o número
# é maior ou menor que 0
if variacao > 0:
    print(f'Houve um crescimento de {variacao}%')
elif variacao < 0:
    print(f'Houve um decrescimento de {variacao}%')
else:
    print('Não houve crescimento ou decrescimento.')
Copiar código
3 - Conseguimos verificar se uma letra é vogal ou consoante verificando se o caractere está contido dentro de uma string de vogais através do operador in.

# Coletamos a letra da pessoa usuária como minúscula
letra = input('Digite uma letra: ').lower()
vogais = 'aeiou' # string contendo todos os dados

# Verificamos se a letra está nas vogais com in
if letra in vogais:
    print('A letra é uma vogal.')
else:
    print('A letra é uma consoante.')
Copiar código
4 - Comparamos cada valor com os outros dois valores referentes aos outros dois anos e determinamos o maior e o menor valor. Fazemos isso atribuindo, inicialmente, a variável preco_ano1 o valor de maior resultado e, caso um haja valor maior que o pré-estabelecido, a variável maior será trocada. A mesma lógica é aplicada à verificação do menor valor.

# Coletamos os preços dos 3 anos
preco_ano1 = float(input('Informe o preço médio do carro no primeiro ano: '))
preco_ano2 = float(input('Informe o preço médio do carro no segundo ano: '))
preco_ano3 = float(input('Informe o preço médio do carro no terceiro ano: '))

# Determinamos o maior valor através de comparações
maior = preco_ano1
if preco_ano2 > maior:
  maior = preco_ano2
if preco_ano3 > maior:
  maior = preco_ano3

# Determinamos o menor valor através de comparações
menor = preco_ano1
if preco_ano2 < menor:
  menor = preco_ano2
if preco_ano3 < menor:
  menor = preco_ano3

# Mostramos o resultado
print(f'O preço mais alto foi de R$ {maior}.')
print(f'O preço mais baixo foi de R$ {menor}.')
Copiar código
5 -

# Coletamos os preços dos três produtos
p1 = float(input('Digite o preço do primeiro produto: '))
p2 = float(input('Digite o preço do segundo produto: '))
p3 = float(input('Digite o preço do terceiro produto: '))

# Verificamos qual produto é o mais barato usando o operador lógico 'and'
if p1 < p2 and p1 < p3:
    print('O primeiro produto é o mais barato.')
elif p2 < p1 and p2 < p3:
    print('O segundo produto é o mais barato.')
elif p3 < p1 and p3 < p2:
    print('O terceiro produto é o mais barato.')
elif p1 == p2 == p3:
    print('Os produtos possuem o mesmo preço.')
else:
    # Identificamos quais produtos possuem o mesmo preço, se for o caso
    if p1 == p2:
        print('O primeiro e o segundo produtos são os mais baratos.')
    elif p2 == p3:
        print('O segundo e terceiro produtos são os mais baratos.')
    elif p1 == p3:
        print('O primeiro e o terceiro produtos são os mais baratos.')
Copiar código
6 - Após coletados os 3 números, fazemos comparações seguindo uma lógica similar à da questão anterior: usamos o operador lógico and para verificar qual o maior valor entre os 3 dados de produto, depois fazemos uma verificação entre os dois menores e, assim, usamos o print para imprimir ordenadamente os números para cada caso, através de várias condicionais agrupadas.

# Coletamos os 3 números
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

# Comparação entre os 3 números
if (num1 >= num2) and (num1 >= num3):
    print(num1)
    if num2 >= num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif (num2 >= num1) and (num2 >= num3):
    print(num2)
    if num1 >= num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
else:
    print(num3)
    if num1 >= num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)
Copiar código
7 -

# Coletamos o turno de estudo
turno = input('Digite em qual turno você estuda (manhã, tarde ou noite): ')

# Comparamos a entrada com todas as opções e imprimimos o resultado.
if turno == 'manhã':
  print('Bom Dia!')
elif turno == 'tarde':
  print('Boa Tarde!')
elif turno == 'noite':
  print('Boa Noite!')
else:
  print('Valor Inválido!')
Copiar código
8 - Podemos usar o operador de módulo % para determinar se um número é par ou ímpar. Se a divisão inteira de um número por 2 tiver um resultado igual à zero, então ele é par. Se não for, ele é ímpar. Isso é possível ser afirmado pois todos os pares são divisíveis por 2, então não há restos na divisão.

# Coletamos os dados
num = int(input('Digite um número: '))

# Verificamos se o número é par através do resultado do módulo
if num % 2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')
Copiar código
9 - Podemos usar o operador de módulo % para determinar se um número é inteiro ou decimal. Se o operador de módulo % retornar zero da divisão inteira de um número por 1, então ele é inteiro. Se não for, ele é decimal.

# Coletamos os dados
num = float(input('Digite um número: '))

# Verificamos se o número é inteiro ou decimal através do resultado do módulo
if num % 1 == 0:
    print('O número é inteiro.')
else:
    print('O número é decimal.')
Copiar código
10 -

# Coletamos os números a serem operados e solicitamos a operação desejada pela pessoa usuária
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
operacao = input('Informe a operação desejada (+, -, *, /): ')

# Verificamos o operador que foi selecionado e executa a operação matemática conforme a seleção
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2
else: # Especificamos um resultado caso a pessoa usuária não digite alguma das operações corretamente.
    print('Operação inválida, resultado da operação será 0')
    resultado = 0 

#  Fazemos as mesmas verificações das questões anteriores para fazer o relatório do cálculo entre números
if resultado % 1 == 0:
    print('O resultado é inteiro.')
else:
    print('O resultado é decimal.')

if resultado > 0:
    print('O resultado é positivo.')
elif resultado == 0:
    print('O resultado é neutro.')
else:
    print('O resultado é negativo.')

if resultado % 2 == 0:
    print('O resultado é par.')
else:
    print('O resultado é ímpar.')
Copiar código
11 - Após coletarmos os valores dos 3 lados de um triângulo, precisamos verificar se ele pode mesmo ser um triângulo seguindo a dica “Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro”. Essa verificação podemos fazer com o operador and. Depois, podemos verificar se todos os lados são iguais formando um equilátero, ou se todos os lados são diferentes, formando um escaleno. Conseguimos executar essas verificações com o operador and e os comparadores == e !=. Por fim, utilizamos o else para o caso de um triângulo isósceles.

# Coletamos os lados de um triângulo
print('Coletaremos os lados de um triângulo.')
lado1 = float(input('Digite o comprimento do primeiro lado: '))
lado2 = float(input('Digite o comprimento do segundo lado: '))
lado3 = float(input('Digite o comprimento do terceiro lado: '))

# Verificamos de os lados formam um triângulo
if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
    print('Os valores podem formar um triângulo!')
    # comparamos os lados para verificar o tipo de triângulo
    if (lado1 == lado2) and (lado2 == lado3):
        print('O triângulo é equilátero.')
    elif (lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
        print('O triângulo é escaleno.')
    else:
        print('O triângulo é isósceles.')
else:
    print('Os valores não podem formar um triângulo!')
Copiar código
12 -

# Coletamos a quantidade de litros e o tipo de combustível,
# já deixando o caractere em maiúsculo para facilitar nossa análise
quantidade_litros = float(input('Informe a quantidade de litros vendidos: '))
tipo_combustivel = input('Informe o tipo de combustível (E para etanol e D para diesel): ').upper()

#  Verificamos primeiro o tipo de combustível
if tipo_combustivel == 'E':
  # Taxamos o valor do preço em litros do etanol
  preco_litro = 1.70
  # De acordo com o valor da quantidade de litros, taxamos também o desconto
  if quantidade_litros <= 15:
    desconto = 0.02
  else:
    desconto = 0.04
elif tipo_combustivel == 'D':
  # Taxamos o valor do preço em litros do disel
  preco_litro = 2.00
  # De acordo com o valor da quantidade de litros, taxamos também o desconto
  if quantidade_litros <= 15:
    desconto = 0.03
  else:
    desconto = 0.05
# Caso ocorra um erro na especificação de tipo de combustível,
# consideramos entradas inválidas, e os preços são taxados em 0
else:
    print('Entradas inválidas!')
    preco_litro = 0
    desconto = 0

# Fazemos o cálculo do valor de desconto, seguido do cálculo do preço descontado
valor_desconto = preco_litro * quantidade_litros * desconto
valor_pago = preco_litro * quantidade_litros - valor_desconto

# Resultado
print(f'Valor a ser pago pelo cliente: R$ {valor_pago}')
Copiar código
13 -

# Coletamos as vendas dos dois anos
venda_2022 = float(input('Informe a quantidade de vendas em 2022: '))
venda_2023 = float(input('Informe a quantidade de vendas em 2023: '))

# Calculamos a variação percentual entre as vendas dos anos de 2022 e 2023
var_percentual = 100 * (venda_2023 - venda_2022) / (venda_2022)

# Análise condicional da variação percentual para determinar a sugestão a ser enviada
if var_percentual > 20:
    print('Bonificação para o time de vendas.')
elif 2 <= var_percentual <= 20:
    print('Pequena bonificação para time de vendas.')
elif -10 <= var_percentual < 2:
    print('Planejamento de políticas de incentivo às vendas.')
else:
    print('Corte de gastos.')