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

<div id="parte3"></div>

# Exercícios - Lista 02 
<p>Devido ao formato dos arquivos, a lista 02 será apresentada através do documento abaixo:</p>
<a href="\lista-de-exercicios\lista-02\Lista_02.ipnb">Lista 02</a>
