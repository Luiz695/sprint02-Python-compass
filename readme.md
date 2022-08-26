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
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
Dica: leia a documentação do pacote json, link: https://docs.python.org/3/library/json.html

```py
import json

with open('./person.json', 'r') as arquivoJson:
    #Parse
    arquivoJson = json.load(arquivoJson)  #Metodo para realizar o parse do arquivo JSON - converte em dicionario
    print('Parse do arquivo Json - tipo atual->dicionário: \n', arquivoJson, '\n')
    print('Tipo de arquivo: \n', type(arquivoJson), '\n')
    
    print('Conteúdo do arquivo Json: \n', arquivoJson['person'], '\n')
      
    #JSON data em Python
    arquivoJsonDumped = json.dumps(arquivoJson, indent=3, ensure_ascii=False) # converte para JSON - STRING
    print('Arquivo JSON: \n', arquivoJsonDumped)
    print(type(arquivoJsonDumped))
```
## Exercício 08
Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida retorna o resultado em uma nova lista. Teste sua função para saber se está ok
```py
def my_map(list,f):
    nova_lista=[]
    
    for elemento in list:
        resultado = f()
        nova_lista.append(resultado)
    return nova_lista  
```
Teste manual:
```py
def default_valor2():
    return 2

def default_valor3():
    return 3

lista = [1, 2, 3, 4]
print(my_map(lista, default_valor2))
print(my_map(lista, default_valor3))
```
Teste unitário:
```py
import unittest
class Testa_funcao_my_map(unittest.TestCase):
    def test_default_2(self):
        self.assertEqual(my_map([1, 2, 3, 4], default_valor2), [2, 2, 2, 2])
    def test_default_3_int(self):
        self.assertEqual(my_map([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_valor3), [3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
    def test_default_3_str(self):
        self.assertEqual(my_map(['a', 'b', 'c', 'd', 'e'], default_valor3), [3, 3, 3, 3, 3])
    
unittest.main(argv=[''], verbosity=2, exit=False)
```
## Exercício 09
Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de
parâmetros nomeados e imprime o valor de cada parâmetro recebido.

```py
def function(*args, **kwargs):
    for item in args:
        print('Parâmetro não nomeado: ', item)
    for key, value in kwargs.items():
        print('Parâmetro nomeado: ', key, value)
        
function('1', 2, True, ['b', 'c'], 6.3, y=7.8, param1=10, param2='hello')
```
## Exercício 10
Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, True se a lâmpada
estiver ligada, False caso esteja desligada. 
A classe Lampada possuí os seguintes métodos:
• liga(): muda o estado da lâmpada para ligada
• desliga(): muda o estado da lâmpada para desligada
• esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
```py
class Lampada(object):
    #construtor
    def __init__(self, ligada = False, status='Lâmpada desligada.'):
        self.ligada = ligada
        self.status = status
        
    def liga(self):
        if self.ligada == True: 
            print("Lâmpada já se encontra ligada.\n")
        else: 
            self.ligada = True 
            self.status = 'Lâmpada ligada.'
            return print('Lâmpada ligada com sucesso. \n') 
      
    def desliga(self):
        if self.ligada == False: 
            print("Lâmpada já se encontra desligada.\n")
        else:
            self.ligada = False 
            self.status = 'Lâmpada desligada'
            return print('Lâmpada desligada com sucesso. \n') 
      
    def esta_ligada(self):
       print(f'Status da Lâmpada: {self.status} \nLigada: {self.ligada} \n')
```

## Exercício 11
Escreva um programa que leia do teclado uma sequência de número separados por vírgula (e.g. 2,4,5,6,1,6) e
imprime a soma de todos eles.

```py
on = True
while True:
    try:
        numero = input("Digite os numeros que deseja somar, separados por virgula: ")
        print('Numeros digitados: ', numero) #print(type(numero)) #string
        lista = numero.split(',')
        lista_numeros = []
        for el in lista:
            lista_numeros.append(float(el) )   
        print('Lista criada: ', lista_numeros)
        print('Soma: ', sum(lista_numeros))
        on = False
        break
    except ValueError:
        print('Valor informado é inválido. Não foi possível realizar a soma. Tente novamente.')
        on = True
```
## Exercício 12
Escreve uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3
partes iguais. Teste sua implementação

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
```py
import time
def divide_lista(lista):
    primeira_posicao = lista[0]
    ultima_posicao = len(lista)
    qtd_elementos = len(lista)
    qtd_lista = (qtd_elementos//3)   
    a, b, c = [], [], []
    
    print('\nEste programa realiza a divisão da lista informada em 3 partes iguais. \nCaso a lista informada não gere listas de mesmo tamanho, sera adicionado um 0 ao final da lista até ser possível realizar a divisão.')
    print('Dividindo a lista...')
    time.sleep(5)
    
    for el in lista:
        #a = lista[:qtd_lista]
        a = lista[:qtd_elementos//3]
        b = lista[qtd_lista: (2*qtd_lista)]
        c = lista[(2*qtd_lista):qtd_elementos]
    if len(a)==len(b) and len(b)==len(c):
        print('Lista dividida com sucesso!\n\nListas:')
        #return f'{a}, {b}, {c}'
        return a, b, c
    else: # len(lista)%3 != 0
        print("\nNão foi possível realizar a divisão da lista em 3 listas de tamanhos iguais.")
        print("Chamando a função novamente...")
        print("Acrescentando um zero na lista...")
        lista.append(0)
        print("Nova lista: ", lista)
        time.sleep(2)
        return (divide_lista(lista))
```

Teste manual:
```py
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16]
#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 18]
print(divide_lista(lista))
```
Teste unitário:
```py
import unittest
class Testa_funcao_Divide_Lista(unittest.TestCase):
    def testFuncaoDivide(self):
        self.assertEqual(divide_lista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), ([1, 2, 3, 4, 5 ],[ 6, 7, 8, 9, 10], [11, 12, 13, 0, 0]))
    
unittest.main(argv=[''], verbosity=2, exit=False)
```
## Exercício 13
```py
```

## Exercício 14
```py
```

## Exercício 15
```py
```

<div id="parte3"></div>

# Exercícios - Lista 02 
<p>Devido ao formato dos arquivos, a lista 02 será apresentada através do documento abaixo:</p>
<a href="\lista-de-exercicios\lista-02\Lista_02.ipnb">Lista 02</a>
