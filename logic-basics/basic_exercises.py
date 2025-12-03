# ==================================================
# Manipulando Dados no Python – Coleta e Amostragem de Dados
# Manipulating Data in Python – Data Collection and Sampling

# ==================================================
# Q1 (PT): Solicite o nome do usuário e imprima "Olá, [nome]!"
# Q1 (EN): Ask the user for their name and print "Hello, [name]!"

nome = input('Digite seu nome: ')
print(f'Olá, {nome}!')
# ---
# Q2 (PT): Solicite o nome e a idade do usuário e imprima "Olá, [nome], você tem [idade] anos."
# Q2 (EN): Ask the user for their name and age, and print "Hello, [name], you are [age] years old."

nome = input('Digite seu nome: ')
idade = int(input('Insira sua idade: '))
print(f'Olá, {nome}, você tem {idade} anos.')
# ---
# Q3 (PT): Solicite o nome, idade e altura do usuário e imprima "Olá, [nome], você tem [idade] anos e mede [altura] metros!"
# Q3 (EN): Ask the user for their name, age, and height in meters, and print "Hello, [name], you are [age] years old and [height] meters tall!"

nome = input('Qual seu nome?: ')
idade = int(input('Qual sua idade?: '))
altura = float(input('Qual a sua altura em metros?: '))
print(f'Olá, {nome}, você tem {idade} anos e mede {altura} metros!')



# ==================================================
# Calculadora com Operadores

# ==================================================
# Q1 (PT): Solicite dois valores e imprima a soma.
# Q1 (EN): Ask for two numbers and print their sum.

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(f'O resultado da soma entre {a} e {b} é: {a+b}')
# ---
# Q2 (PT): Solicite três valores e imprima a soma.
# Q2 (EN): Ask for three numbers and print their sum.

a = int(input('Qual o primeiro valor?: '))
b = int(input('Qual o segundo valor?: '))
c = int(input('Qual o terceiro valor?: '))
print(f'O resultado entre a soma de {a}, {b} e {c} é igual a: {a+b+c}')
# ---
# Q3 (PT): Solicite dois valores e imprima a subtração do primeiro pelo segundo.
# Q3 (EN): Ask for two numbers and print the subtraction of the first minus the second.

a = int(input('Qual o primeiro valor?: '))
b = int(input('Qual o segundo valor?: '))
print(f'A subtração do valor {a} do valor {b} é igual a: {a-b}')
# ---
# Q4 (PT): Solicite dois valores e imprima a multiplicação.
# Q4 (EN): Ask for two numbers and print the multiplication.

a = int(input('Qual o primeiro valor?: '))
b = int(input('Qual o segundo valor?: '))
print(f'O resultado da multiplicação entre {a} e {b} é igual a {a*b}')
# ---
# Q5 (PT): Solicite numerador e denominador e realize a divisão. Denominador não pode ser 0.
# Q5 (EN): Ask for numerator and denominator and perform division. Denominator cannot be 0.

a = int(input('Qual o numerador?: '))
b = int(input('Qual o denominador diferente de 0?: '))
print(f'O resultado da divisão entre o valor {a} e {b} é igual a {a/b}')
# ---
# Q6 (PT): Solicite base e expoente e realize a exponenciação.
# Q6 (EN): Ask for base and exponent and calculate the power.

a = int(input('Qual o operador?: '))
b = int(input('Qual a potência?: '))
print(f'O valor de {a} elevado a {b} potência é igual a: {a**b}')
# ---
# Q7 (PT): Solicite numerador e denominador e realize a divisão inteira. Denominador não pode ser 0.
# Q7 (EN): Ask for numerator and denominator and perform integer division. Denominator cannot be 0.

a = int(input('Qual o numerador?: '))
b = int(input('Qual o denominador diferente de 0?: '))
print(f'O valor de {a} dividido pra {b} é igual a {a//b}')
# ---
# Q8 (PT): Solicite numerador e denominador e retorne o resto da divisão. Denominador não pode ser 0.
# Q8 (EN): Ask for numerator and denominator and return the remainder. Denominator cannot be 0.

a = int(input('Qual o numerador?: '))
b = int(input('Qual o denominador diferente de 0?: '))
print(f'O valor de {a} dividido por {b} é igual a {a/b}, e o resto é {a%b}')
# ---
# Q9 (PT): Solicite 3 notas e imprima a média.
# Q9 (EN): Ask for 3 grades and print the average.

a = float(input('Qual a nota de João?: '))
b = float(input('Qual a nota de Maria?: '))
c = float(input('Qual a nota de Pedro?: '))
print(f'A média entre as notas de João, Maria e Pedro é igual a {(a+b+c)/3}')
# ---
# Q10 (PT): Calcule e imprima a média ponderada de 5, 12, 20 e 15 com pesos 1, 2, 3 e 4.
# Q10 (EN): Calculate and print the weighted average of 5, 12, 20, and 15 with weights 1, 2, 3, and 4.

media_pon = (5*1 + 12*2 + 20*3 + 15*4) / (1+2+3+4)
print(f'A média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4 é equivalente a: {media_pon}')



# ==================================================
# Editando Textos
# Editing Texts
# ==================================================
# Q1 (PT): Crie uma variável com uma frase e imprima-a.
# Q1 (EN): Create a variable with a sentence and print it.

frase = 'Olá Mundo!'
print(frase)
# ---
# Q2 (PT): Solicite uma frase e imprima-a.
# Q2 (EN): Ask for a sentence and print it.

frase = input('Digite uma frase: ')
print(frase)
# ---
# Q3 (PT): Solicite uma frase e imprima em maiúsculas.
# Q3 (EN): Ask for a sentence and print it in uppercase.

frase = input('Digite uma frase: ')
print(frase.upper())
# ---
# Q4 (PT): Solicite uma frase e imprima em minúsculas.
# Q4 (EN): Ask for a sentence and print it in lowercase.

frase = input('Digite uma frase: ')
print(frase.lower())
# ---
# Q5 (PT): Crie uma variável com uma frase e imprima-a sem espaços no início e fim.
# Q5 (EN): Create a variable with a sentence and print it without leading or trailing spaces.

frase = ' Olá mundo  '
print(frase.strip())
# ---
# Q6 (PT): Solicite uma frase e imprima-a sem espaços no início e fim.
# Q6 (EN): Ask for a sentence and print it without leading or trailing spaces.

frase = input('Digite uma frase: ')
print(frase.strip())
# ---
# Q7 (PT): Solicite uma frase e imprima-a sem espaços no início e fim e em maiúsculas.
# Q7 (EN): Ask for a sentence and print it stripped and in uppercase.

frase = input('Digite uma frase: ')
print(frase.strip().upper())
# ---
# Q8 (PT): Solicite uma frase e substitua todas as letras "e" por "f".
# Q8 (EN): Ask for a sentence and replace all "e" letters with "f".

frase = input('Digite uma frase: ')
print(frase.replace('e', 'f'))
# ---
# Q9 (PT): Solicite uma frase e substitua todas as letras "a" pelo caractere "@".
# Q9 (EN): Ask for a sentence and replace all "a" letters with "@".

frase = input('Digite uma frase: ')
print(frase.replace('a', '@'))
# ---
# Q10 (PT): Solicite uma frase e substitua todas as consoantes "s" pelo caractere "$".
# Q10 (EN): Ask for a sentence and replace all consonants "s" with "$".

frase = input('Digite uma frase: ')
print(frase.replace('s', '$'))
# ---
# Q11 (PT): Peça ao usuário sua idade em anos e calcule quantos dias ele já viveu (aproximando cada ano como 365 dias).
# Q11 (EN): Ask the user for their age in years and calculate how many days they have lived (approximating each year as 365 days).

idade = int(input('Qual sua idade?: '))
print(f'Com {idade}, você já viveu {idade*365} dias!')
# ---
# Q12 (PT): Peça ao usuário para inserir: salário mensal, gasto com alimentação, gasto com transporte, gasto com lazer.
# Depois, calcule: total de gastos, saldo restante do salário, percentual do salário gasto em cada categoria.
# Q12 (EN): Ask the user to input: monthly salary, spending on food, spending on transport, and spending on leisure.
# Then, calculate: total expenses, remaining salary, percentage of salary spent on each category.

sal_men = float(input('Qual o seu salário mensal?: '))
gast_ali = float(input('Qual foi o seu gasto mensal com alimentação?: '))
gast_tran = float(input('Qual foi o seu gasto com transporte?: '))
gast_laz = float(input('Qual foi o seu gasto com lazer?: '))
total = gast_ali+gast_tran+gast_laz
restante = sal_men-total
perc_gast_ali = (gast_ali / sal_men)*(100)
perc_gast_tran = (gast_tran / sal_men)*(100) 
perc_gast_laz = (gast_laz / sal_men)*(100) 
print(f'O total de gastos do mês é: R${total:.2f}')
print(f'O saldo restante do salário é: R${restante:.2f}')
print(f'O percentual do salário gasto em cada categoria é igual a {perc_gast_ali:.2f}% em alimentação, {perc_gast_tran:.2f}% em transporte e {perc_gast_laz:.2f}% em lazer!')
# ---
# Q13 (PT): Peça ao usuário para informar uma distância em quilômetros. Depois, converta para metros e centímetros.
# Q13 (EN): Ask the user to input a distance in kilometers. Then, convert it to meters and centimeters.

quilog = float(input('Insira quantos quilômetros você percorreu: '))
metros = quilog*1000
cent = metros*100
quilog_fmt = f"{quilog:,.0f}".replace(',', '.')
metros_fmt = f"{metros:,.0f}".replace(',', '.')
cent_fmt = f"{cent:,.0f}".replace(',', '.')
print(f'Em {quilog_fmt} quilômetros você percorreu o equivalente a {metros_fmt} metros, justamente {cent_fmt} centímetros.')



# ==================================================
# Aquecendo na Programação
# Warming Up in Programming

# ==================================================
# Q1 (PT): Peça dois números ao usuário e exiba qual deles é maior.
# Q1 (EN): Ask the user for two numbers and display which one is greater.

num1 = int(input('Qual o primeiro número?: '))
num2 = int(input('Qual o segundo número?: '))

if num1 > num2:
    print(f'O maior número entre {num1} e {num2} é: {num1}')
elif num2 > num1:
    print(f'O maior número entre {num1} e {num2} é: {num2}')
else:
    print('Os dois números são iguais')
# ---
# Q2 (PT): Solicite o percentual de crescimento e informe se é positivo, negativo ou nulo.
# Q2 (EN): Ask for the growth percentage and state whether it is positive, negative, or zero.

percen = float(input('Qual o percentual de crescimento de produção da empresa?: '))

if percen > 0:
    print('O percentual tem porcentagem positiva!')
elif percen < 0:
    print('O percentual tem porcentagem negativa!')
else:
    print('Não houve crescimento ou decrescimento!')

