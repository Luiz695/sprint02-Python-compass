<h1>Sprint 02 - Python</h1>
<p>Diretório referente a entrega das atividades.</p></br>
<h3>Listas de exercicios</h3>
<a href="\lista-de-exercicios\lista-01-01\Lista_01-Parte_01.ipynb">Lista 01 - Parte 01</a></br>


<h3>Sumário</h3>
<a href=#parte1>Exercícios – Parte 1<a>

<div id="parte1"></div>

# Exercícios – Parte 1

## Exercício 1
Escreva um código Python que lê do teclado o nome e a idade de um usuário e imprime o ano em que o
usuário completará 100 anos.
Dica: você pode ler strings digitadas no teclado utilizando a função builtin input('mensagem'). Lembre-se de converter números para seu respectivo tipo (int ou float) antes fazer operações aritméticas.

```sh
import datetime

current_time = datetime.datetime.now()
ano_atual = current_time.year

nome = input('Insira seu nome: ')
idade = int(input('Insira usa idade: '))
ano = 100-idade+2022;
print(f'{nome} irá completar 100 anos em {ano}.')
```
</br>

## Exercício 2
Escreva um código Python que lê do teclado um número digitado pelo usuário e imprime se ele par ou ímpar

```sh
numero = float(input('Digite um numero: '))
if (numero%2==0):
  print(f'{numero} é par.')
else :
  print(f'{numero} é impar.')
```

<br>

## Exercício 3
Escreva um código Python que imprime os números pares de 0 até 20 (incluso).
Dica: olhe a documentação da função range(). Mais informações no link

```sh
for numeros in range(0,21, 2):
  print(numeros)
```

<br>

## Exercício 4
Escreva um código Python que imprime todos os números primos de 0 até 100.

```sh
for numero in range(2, 101):
    for count in range(2, numero):
        if (numero%count) == 0: #o numero possui um divisor sem ser 1 e ele mesmo.
            break # encerra o laço
    else:
        print(f'{numero} é primo')
```

<br>

## Exercício 5

```sh
dia = input('Insira o dia: ')

mes = int(input('Insira o mês: '))
if mes >= 13:
    mes = input('Valor incorreto. Insira novamente o mês: ')
    
ano = input('Insira o ano com quatro digitos: ')
qtd_caracteres_ano = len(ano)
if qtd_caracteres_ano<4:
    ano = input('Insira novamente o ano com quatro digitos: ')
    
print("{:0>2}/{:0>2}/{}".format(dia, mes, ano))
```
