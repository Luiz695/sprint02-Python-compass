<h1>Sprint 02 - Python</h1>
<p>Diretório referente a entrega das atividades.</p>
<h3>Listas de exercicios</h3>
<a href="\lista-de-exercicios\lista-01-01\Lista_01-Parte_01.ipynb">Lista 01 - Parte 01</a></br>
<a href="\lista-de-exercicios\lista-01-02\Lista_01-Parte_02.ipynb">Lista 01 - Parte 02</a></br>
<a href="\lista-de-exercicios\lista-02\Lista_02.ipynb">Lista 02 - Complementares</a>
</br>
</br>
<h3>Diretório de estudos:</h3>
<a href="https://github.com/annekarolinefc/python">Diretório de Python</a></br>
</br>
<h3>Sumário</h3>
<a href=#parte1>Exercícios - Lista 01 – Parte 1</a></br>
<a href=#parte2>Exercícios - Lista 01 – Parte 2</a></br>
<a href=#parte3>Exercícios - Lista 02 - Numpy</a>
<a href=#parte4>Exercícios - Lista 02 - Pandas</a>
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
<br>

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
<br>

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
<br>

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
<br>

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
<br>

## Exercício 06
Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
Dica: leia documentação da função open(...), link: https://docs.python.org/3/library/functions.html#open

```py
arquivo = open('arquivo_texto.txt', 'r')
for line in arquivo.readlines():
    print(line) 
arquivo.close()
```
<br>

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
<br>

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
<br>

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
<br>

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
<br>

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
<br>

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
<br>

## Exercício 13
Dado o dicionário a seguir:
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores
duplicados.

```py
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
c = []
for key, value in speed.items():
    if value in c:
        continue 
    else:
        c.append(value)
print('Lista: ', c)
```
<br>

## Exercício 14
Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!

Usando o modulo statistics para o cálculo da mediana:

```py
import random
import statistics

lista = random.sample(range(500),50)
print('Lista Informada: ', lista, '\n')
print("Valor minimo: ",  min(lista))
print("Valor máximo: ", max(lista))
print("Valor médio: ", (sum(lista)/len(lista)))
print("Valor mediana: ", statistics.median(lista))
```
Resolução utilizando numPy:
```py
import numpy as np 

lista = random.sample(range(500),50)
array = np.array(lista)
print('Array: ', array)
print('Valor mínimo: ', np.min(array))
print('Valor máximo: ', np.max(array))
print('Valor médio: ', np.mean(array))
print('Valor mediana: ', np.median(array))
```
<br>

## Exercício 15
Imprima a lista da célula abaixo de trás para frente.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```py
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a[::-1])
```
ou
```py
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a.reverse()
print(a)
```
<br>

<div id="parte3"></div>

# Exercícios - Lista 02 - numPy

## Exercício 01
Crie um array 5x5 com a sequência 1...25 (incluso) e faça a soma dos elementos da diagonal.
```py
import numpy as np

array = np.array(range(1,26))
new_array= array.reshape((5, 5))
diagonal = np.diagonal(new_array)

print('Array: \n', array, '\n Forma do array (linhas, colunas):', array.shape, '\n')
print('Array 5 x 5: \n', new_array, '\n Forma do array (linhas, colunas): ', new_array.shape, '\n')
print('Diagonal do Array: \n', diagonal, '\n')
print('Soma dos elementos da diagonal: ', np.sum(diagonal)) 
```
ou
```py
array = np.arange(1,26).reshape(5,5)
soma_diagonal = np.trace(array)
print('Array 5 x 5: \n', array, '\n Forma do array (linhas, colunas): ', array.shape, '\n')
print('Soma dos elementos da diagonal: ', soma_diagonal)
```
<br>

## Exercício 02
Crie um array 5x5 com a sequência de números pares entre 0...50 (incluso) e faça as seguintes operações:
• Soma das linhas
• Soma das Colunas
• Média dos elementos da última linha
• Média dos elementos da última coluna

```py
import numpy as np

# NÃO É POSSÍVEL CONSIDERAR O 50 -> array = np.array(range(0, 51, 2))
array = np.array(range(0, 50, 2)).reshape((5, 5))

print('Array: \n', array, '\n')
print('Soma das linhas: ', np.sum(new_array, axis=1))
print('Soma das colunas: ', np.sum(new_array, axis=0))
print("Média dos elementos da ultima linha: ", np.mean(new_array[4], axis=0))
print("Média dos elementos da ultima coluna: ", np.mean(new_array[:,4]))
```
<br>

## Exercício 03
Dado o array 2D abaixo, substitua o seu maior valor por 0.
• np.random.normal(0, 3, size=(5, 5))
```py
import numpy as np

array = np.random.normal(0, 3, size=(5, 5))
print('Array Numpy: \n', array, '\n')
max_el = np.max(array)
print('Maior elemento do array: \n', max_el, '\n')
array[array == max_el] = 0
print('Substituindo valores: \n', array )
```
<br>

## Exercício 04
A partir das arrays abaixo, caso seja possível, realize o produto das mesmas:
• np.random.uniform(size=(5, 3))
• np.random.uniform(size=(3, 4))
```py
import numpy as np

array_1 = np.random.uniform(size=(5, 3)) # m x n
array_2 = np.random.uniform(size=(3, 4)) # n x p
array_3 = array_1.dot(array_2) # M1.dot(M2) | M1 @ M2 
print('Array Numpy 01: \n', array_1, '\n')
print('Array Numpy 02: \n', array_2, '\n')
print('Produto dos Arrays Numpy: \n', array_3, '\n', 'Forma do array: ', array_3.shape, '\n')
```

<br>

## Exercício 05
Dado o array abaixo, converta-o para um array do tipo int32.
• np.arange(9, dtype=np.float32).reshape(3, 3)
```py
import numpy as np

array = np.arange(9, dtype=np.float32).reshape(3, 3)
print('Array Numpy: \n', array, '\n')
print('Tipo de dado do Array: ', array.dtype, '\n')

print('List: \n', array.tolist(), '\n')
list_to_array = np.array(array.tolist(), dtype=np.int32)
print('Array Numpy convertido: \n', list_to_array, '\n')
print('Tipo de dado do Array Convertido: ', list_to_array.dtype)

```
<br>

## Exercício 06
Dado o array abaixo, some 10 em todos os elementos da última coluna.
• np.random.uniform(size=(8, 8))
```py
import numpy as np

array = np.random.uniform(size=(8, 8))
ultima_coluna = array[:,7]
soma_ultima_coluna = (array[:,7]+10)
remove_coluna = np.delete(array, 7, 1)
print('Array Numpy: \n', array, '\n')
print("Última coluna do Array antes da soma: \n", ultima_coluna, '\n')
print("Última coluna do Array após a soma: \n", soma_ultima_coluna)
```
<br>

## Exercício 07
Dados os dois arrays 2x4 abaixo, empilhe ambos formando um novo array 4x4.
• np.array([[0,3,4,5], [7, 10, 9, 2]])
• np.array([[1,4,9,12], [15, 22, 19, 17]])

```py
import numpy as np

array_01 = np.array([[0,3,4,5], [7, 10, 9, 2]])
array_02 = np.array([[1,4,9,12], [15, 22, 19, 17]])
array_03 = np.concatenate((array_01, array_02))
print('Array Numpy 01: \n', array_01, '\n', 'Forma do array numpy (linhas, colunas): \n', array_01.shape, '\n')
print('Array Numpy 02: \n', array_02, '\n', 'Forma do array numpy (linhas, colunas): \n', array_02.shape, '\n')
print('New Array Numpy: \n', array_03, '\n', 'Forma do array numpy (linhas, colunas): \n', array_03.shape)
```
<br>

## Exercício 08
Dado o array definido por np.arange(25).reshape(5, 5), realize as seguintes operações sem utilizar nenhum tipo de loop (for / while):
• A média das linhas 0, 2 e 3.
• A média das colunas 0, 1 e 4.
• A soma dos elementos das duas diagonais.
```py
import numpy as np

array = np.arange(25).reshape(5, 5)
media_linhas = np.mean(array, axis = 1)

print('Média das linhas: ', np.mean(array))
print('Média de cada linha: ', array.mean(axis=1) )
print('Média da linha 0: ',  np.mean(array[0,:]))
print('Média da linha 2: ',  np.mean(array[2,:]))
print('Média da linha 3: ',  np.mean(array[3,:]), '\n')

print('Média das colunas: ', np.mean(array.mean(axis=0)))
print('Média de cada coluna: ', array.mean(axis=0) )
print('Média da coluna 0: ', np.mean(array[:,0]))
print('Média da coluna 1: ', np.mean(array[:,1]))
print('Média da coluna 4: ', np.mean(array[:,4]), '\n')

diagonal = np.trace(array)
diagonal2 = np.trace(array, axis2=1) # eixo
soma_diagonal = diagonal+diagonal2
print("A soma dos elementos das duas diagonais é: ", soma_diagonal)
```
<br>

## Exercício 09
Dado o array abaixo, selecione os valores Pares e todos os valores maiores que 8, seu código não deve conter nenhum tipo de loop (for / while):

• np.arange(25).reshape(5, 5)
```py
import numpy as np

array = np.arange(25).reshape(5, 5)
new_array = array[(array%2==0)&(array>8)]
print('Array Numpy: \n', array, '\n')
print('Seleção de valores pares e valores > 8 do Array Numpy: \n', new_array, '\n')
```

## Exercício 10
Dado o array 2D abaixo, substitua os 5 menores valores por -1, seu código não deve conter nenhum tipo de loop (for / while):
• a = np.random.randint(0, 50, (5, 5))
```py
import numpy as np 

array = np.random.randint(0, 50, (5, 5))
print('Array Numpy: \n', array, '\n')
lista = array.ravel().tolist() #array.reshape(-1)
print("Lista: \n", lista)
lista_ordenada = sorted(lista)
print("Lista ordenada: ", lista_ordenada, '\n')
cinco_menores = lista_ordenada[:5] 
print("Cinco menores: ", cinco_menores)
#lista_ordenada[:5] = -1
lista_ordenada[0] = -1
lista_ordenada[1] = -1
lista_ordenada[2] = -1
lista_ordenada[3] = -1
lista_ordenada[4] = -1
print("Lista ordenada com valores substituidos: ", lista_ordenada, '\n')
novo_array= np.array(lista_ordenada).reshape((5, 5))
print('Resultado final: \n', novo_array)
```
</br>
</br>

# Exercícios - Lista 02 - Pandas
<a href="\lista-de-exercicios\lista-02\Lista_02.ipnb">Lista 02</a>

## Exercício 1
Leia o arquivo actors.csv e faça os seguintes cálculos sobre o conjunto de dados utilizando Pandas


• O ator/atriz com maior número de filmes e o respectivo número de filmes.
```py
df_2 = df[['Actor', 'Number of Movies', '#1 Movie']]
max = df_2.max()
df_filtro = df_2['Number of Movies']==maior_qtd_filmes
df_ator = df_2[df_filtro]
df_ator
```

• A média do número de filmes.
```py
df_mean_number_of_movies = df[['Number of Movies']]
media = np.mean(df_mean_number_of_movies)
serie_conferencia = pd.Series(data=media)
df_media = df_mean_number_of_movies.mean()
print('A média do número de filmes é:', serie_conferencia)
```
• O ator/atriz com a maior média por filme.
```py
df_actor_average = df[['Actor', 'Average per Movie']]
max_average = df['Average per Movie'].max()
df_filtro = df_actor_average['Average per Movie']==max_average
df_autores = df_actor_average[df_filtro]
df_autores
```
• O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
Exibindo os 7 filmes mais frequentes e sua frequência:
```py
df_filmes = df[['#1 Movie']]
df_2 = df_filmes.sort_values(by='#1 Movie', ascending=False)
df_3 = df_2.value_counts()
print("Os 7 filmes mais frequentes")
df_filmes_mais_frequentes = df_3.head(7)
df_filmes_mais_frequentes
```
<div id="parte4"></div>
## Exercício 2

Exercício 2
Leia o arquivo csv googleplaystore.csv e realize as seguintes atividades sobre o dataset utilizando Pandas:
• Faça um gráfico de barras contendo os top 5 apps por número de instalação.
```py
# df['Installs'] está como objeto. NECESSÁRIO transformar em float.
#print("Tipo de dados da Coluna de Número de Instalações: \n", df['Installs'].dtype)
df['Installs'] = df['Installs'].apply(lambda x: str(x).replace(',', ''))
df['Installs'] = df['Installs'].astype(float)

#Criação do DataFrame utilizado
df_apps_instalações = df[["App","Installs"]]

#print("Relação de aplicativos e número de instalações: \n", df_apps_instalações)
df_apps_instalações_agrupados = df_apps_instalações.groupby('App').sum()
df_apps_instalações_agrupados

#Ordenando por número de instalações
top_5_apps = df_apps_instalações_agrupados.nlargest(5, columns="Installs").head(5)
print("Os TOP 5 apps por número de instalação são: \n")
top_5_apps
```
Plotando o gráfico:
```py
import matplotlib.pyplot as plt 

top_5_apps.plot.bar(colormap='Accent',title='Top 5 aplicativos', ylabel='Quantidade de Instalações')
```

![image](/lista-de-exercicios//lista-02/top_5_app.png)


• Faça um gráfico de pizza (pie chart) mostrando as categorias de apps existentes no dataset de acordo com a frequência em que elas aparecem.
Conforme o código abaixo, há somente UMA categoria de app no dataset.
```py
# Contar numero de categorias
categorias_dos_apps = df[['Category']]
# Contando 
contagem = categorias_dos_apps.value_counts()
categoria_de_apps_group = categorias_dos_apps.groupby(['Category']).count()
categoria_de_apps_group
```
Essa categoria, foi separada em gêneros. Portanto, as categorias dentro do gênero Game são:
```py
# Contar numero de categorias
genero_dos_apps = df[['Genres']].replace(',', '')

# Contando 
contagem = genero_dos_apps.value_counts()
contagem = contagem.to_frame()
contagem
```
O gráfico abaixo, representa essas categorias:
![image](/lista-de-exercicios/lista-02/categoria_de_generos_do_app.png)
• Mostre qual o app mais caro existente no dataset.
```py
#Transformando o tipo de dado da coluna de preço e removendo strings indesejadas
print(df['Price'].dtype)
df['Price'] = df['Price'].apply(lambda x: str(x).replace(',', '').strip('$'))
df['Price'] = df['Price'].astype(float)
print(df['Price'].dtype)
#O critério utilizado para a resolução é o Price - #preco_mais_caro = max(df['Price'])
preco_mais_caro=pd.to_numeric(df['Price'])
#Obtendo o index do app mais caro
app_caro = preco_mais_caro.idxmax()
# Criando um dataframe para o app mais caro
df_do_app = df.loc[app_caro].to_frame()
df_do_app
```
• Mostre quantos apps são classificados como “Mature 17+”.
Os app classificados como "Mature 17+" são obtidos a partir de:
```py
df_resolucao = df[['App', 'Content Rating']]
classificados = df_resolucao[df_resolucao['Content Rating']=='Mature 17+'] #classificados_2 = df_resolucao.loc[df_resolucao['Content Rating']=='Mature 17+']
quantidade_app_classificado = classificados.groupby('Content Rating').value_counts()
classificados
```
É um total de 63 aplicativos:
```py
df_resolucao = df_resolucao.drop_duplicates('App')
classificacao = df[['Content Rating']].value_counts().loc['Mature 17+']
classificacao
```
• Mostre o top 10 apps por número de reviews bem como o respectivo número de reviews. Ordene a lista de forma decrescente por número de reviews.
```py
df_resolucao = df[['App','Reviews']]
df_resolucao_2 = df_resolucao.sort_values(by='Reviews', ascending=False )
df_resolucao_3 = df_resolucao_2.groupby('App').sum()
df_resolucao_3 = df_resolucao_3.sort_values(by='Reviews', ascending=False )
df_resolucao_3 = df_resolucao_3.head(10)
```
Plotando o gráfico:
![image](/lista-de-exercicios/lista-02/top_10_app_por_n%C3%BAmero_de_reviews.png)
```py
df_resolucao_3.plot.pie(title = "Categoria dos Aplicativos", figsize=(8, 8), autopct='%1.1f%%', subplots = True, legend = True)
```
