<h1>Sprint 02 - Python</h1>
<p>Diretório referente a entrega das atividades.</p>
<h3>Listas de exercicios</h3>
<a href="\lista-de-exercicios\lista-01-01\Lista_01-Parte_01.ipynb">Lista 01 - Parte 01</a>
<a href="\lista-de-exercicios\lista-01-02\Lista_01-Parte_02.ipynb">Lista 01 - Parte 02</a>
<a href="\lista-de-exercicios\lista-02\Lista_02.ipnb">Lista 02</a>
</br>
<h3>Diretório de estudos:</h3>
<a href="https://github.com/annekarolinefc/python">Diretório de Python</a>
</br>
<h3>Sumário</h3>
<a href=#parte1>Exercícios - Lista 01 – Parte 1</a>
<a href=#parte3>Exercícios - Lista 01 – Parte 2</a>
<a href=#parte2>Exercícios - Lista 02</a>
</br>
</br>

<div id="parte1"></div>

# Exercícios - Lista 01 – Parte 1

## Exercício 1
Escreva um código Python que lê do teclado o nome e a idade de um usuário e imprime o ano em que o
usuário completará 100 anos.
Dica: você pode ler strings digitadas no teclado utilizando a função builtin input('mensagem'). Lembre-se de converter números para seu respectivo tipo (int ou float) antes fazer operações aritméticas.

```py
import datetime
on = True
while (on): 
    try:
        current_time = datetime.datetime.now()
        current_time_1 = current_time.year
        name = input('Insira seu nome: ')
        age = int(input('Insira usa idade: '))
        year = 100-age+current_time_1;
        print(f'{name} irá completar 100 anos em {year}.')
        on=False
    except ValueError:
        print('Valor digitado é invalido')
```
</br>

## Exercício 2
Escreva um código Python que lê do teclado um número digitado pelo usuário e imprime se ele par ou ímpar

```py
funcionando = True
while (funcionando):
    try:
        numero = float(input('Digite um numero: '))
        if (numero%2==0):
            print(f'{numero} é par.')
            x = input('Deseja realizar uma nova busca: S/N')
            if (x.upper() == 'S'):
                funcionando = True 
                continue
            else:
                funcionando = False
        else :
            print(f'{numero} é impar.')
            x = input('Deseja realizar uma nova busca: S/N')
            if (x.upper() == 'S'): 
                funcionando = True
                continue
            else:
                funcionando = False
    except ValueError:
        print('Erro na execução. Informe um valor válido.')
```

<br>

## Exercício 3
Escreva um código Python que imprime os números pares de 0 até 20 (incluso).
Dica: olhe a documentação da função range(). Mais informações no link

```py
for numeros in range(0,21, 2):
  print(numeros)
```

<br>

## Exercício 4
Escreva um código Python que imprime todos os números primos de 0 até 100.

```py
for numero in range(2, 101):
    for count in range(2, numero):
        if (numero%count) == 0: 
            break 
    else:
        print(f'{numero} é primo')
```

<br>

## Exercício 5

```py
on = True
while True:
    try:
        dia = int(input('Insira o dia: '))

        mes = int(input('Insira o mês: '))
        if mes >= 13:
            mes = input('Valor incorreto. Insira novamente o mês: ')  
        ano = input('Insira o ano com quatro digitos: ')
        qtd_caracteres_ano = len(ano)
        if qtd_caracteres_ano<4:
            ano = input('Insira novamente o ano com quatro digitos: ')
        print("{:0>2}/{:0>2}/{}".format(dia, mes, ano))
        on = False
        break    
    except:
        on = False
        on = True
        print("Valor informado é inválido. Reiniciando a aplicação...")
```

<div id="parte2"></div>

# Exercícios - Lista 01  – Parte 2
## Exercício 1

Dada duas listas como no exemplo abaixo:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Escreve um programa que retorne o que as listas têm comum (sem repetições). O seu programa deve
funcionar para listas de qualquer tamanho.

Resolução utilizando listas:
```py
a, b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
elementos_em_comum, elementos_em_comum_sem_repeticao = [], []

for elem_a in a:
    for elem_b in b:
        if elem_a==elem_b:
            elementos_em_comum.append(elem_a)

for el in elementos_em_comum:
    if el not in elementos_em_comum_sem_repeticao:
        elementos_em_comum_sem_repeticao.append(el)
        
print('Elementos em comum', elementos_em_comum)
print('Elementos em comum sem repetição: ', elementos_em_comum_sem_repeticao)
```
Resolução utilizando conjuntos:
```py
a, b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set(a).intersection(set(b))
print('Elementos em comum sem repetição: ', list(c))
```
## Exercício 2
Dada a seguinte lista:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Faça um programa que gere uma nova lista contendo apenas números ímpares.

Resolução utilizando iteração:
```py
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista_numeros_impares = []

for x in a:
    if (x%2!=0):
        lista_numeros_impares.append(x)
        
print(lista_numeros_impares)
```
Resolução utilizando List Comprehesion
```py
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[x for x in a if x % 2 !=0 ]
```
## Exercício 3
Peça para o usuário digitar uma palavra pelo teclado e determina se a palavra digitada é ou não um
palíndromo. 
Um palíndromo é uma palavra que permanece igual se lida de traz pra frente.

Há diversas formas de implementação para obter se uma palavra é palíndromo ou não. Abaixo será apresentada uma das formas. As outras duas formas estão no arquivo Lista_01-Parte_02.
```py
on = True
while True:
    try:
        palavra = input('Digite uma palavra: ').replace(' ','').lower()
        if palavra == ''.join(reversed(palavra)):
            print("A palavra digitada é um palíndromo.")
        else:
            print("A palavra digitada não é um palíndromo.")
        on = False
        break
    except ValueError:
        print("Erro na aplicação. A aplicação será finalizada.")
        break
```
## Exercício 04
Dada as listas a seguir:
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
Faça um programa que imprima os dados na seguinte estrutura: " - está com anos"

Resolução utilizando loop
```py
primeirosNomes, sobrenomes, idades = ['Joao', 'Douglas', 'Lucas', 'José'], ['Soares', 'Souza', 'Silveira', 'Pedreira'], [19, 28, 25, 31]

x=0
while x<len(idades):
    print(f'{primeirosNomes[x]} {sobrenomes[x]} está com {idades[x]} anos.')
    x+=1
```
Resolução utilizando iteração e zip()
```py
primeirosNomes, sobrenomes, idades = ['Joao', 'Douglas', 'Lucas', 'José'], ['Soares', 'Souza', 'Silveira', 'Pedreira'], [19, 28, 25, 31]
for primeirosNomes, sobrenomes, idades in zip(primeirosNomes, sobrenomes, idades):
    print(f'{primeirosNomes} {sobrenomes} está com {idades} anos.')
```

## Exercício 05
Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize um
exemplo para testar sua função
```py
def nova_lista(lista):    
    lista_conjunto = set(lista)
    nova_lista_conjunto = lista_conjunto
    
    nova_lista = list(nova_lista_conjunto)              
    return nova_lista
```
Teste manual:
```py
lista = [1, 1, 2, 3, 4]
print('Lista original:', lista)
print('Nova Lista:', nova_lista(lista))
```
Teste unitário para testar a função implementada:
```py
import unittest

class TestNovaLista(unittest.TestCase):
    def nova_lista_test(self, lista):
        listaTeste = [1, 1, 2, 3, 4]
        self.assertTrue(listaTeste==lista) 
    
unittest.main(argv=[''], verbosity=2, exit=False)
```
## Exercício 06
Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
Dica: leia documentação da função open(...), link: https://docs.python.org/3/library/functions.html#open

```py
arquivo = open('arquivo_texto.txt', 'r')
for line in arquivo.readlines():
    print(line) 
arquivo.close()
```
## Exercício 07
```py
```
## Exercício 08
```py
```
## Exercício 09
```py
```

```py
```

```py
```

```py
```

<div id="parte3"></div>

# Exercícios - Lista 02 
<p>Devido ao formato dos arquivos, a lista 02 será apresentada através do documento abaixo:</p>
<a href="\lista-de-exercicios\lista-02\Lista_02.ipnb">Lista 02</a>
