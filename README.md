# Tools
Scripts curtos, e úteis.

<details>
  <summary> LISTAR ARQUIVOS </summary><br>

O código lista todos arquivos disponiveis em uma pasta(de sua preferencia).<br>

O script le o nome dos arquivos presentes, e usando with open, armazena toda informação em um arquivo de texto.<br>

```python
import glob # Módulo glob

# PROCURA NO DIRETORIO TODOS ARQUIVOS.
listar_arquivo = glob.glob('*.*') # No trecho " glob.glob('*.*') " Existem dois asteriscos:
    # 1º Nome do Arquivo
    # 2° Nome da Extensão

with open("Lista_Nome_Arquivos.txt","w") as f:
    for linha in listar_arquivo:
        f.write(linha+"\n")
```

  Para instalar o módulo digite:<br>
  ```  $ pip install glob2  ```
  
</details>

<details>
  <summary> ENVIAR E-MAIL (smtplib)</summary><br>
  
  Envia e-mail via Python.<br>

```python
import smtplib

server = smtplib.SMTP('smtp.gmail.com:587') # GOOGLE
#server = smtplib.SMTP("smtp.live.com:587") # OUTLOOK

server.starttls()
endmail = "" # SEU ENDEREÇO DE E-MAIL 
pswd = "" # SUA SENHA
from_mail = "" # ENDEREÇO DE E-MAIL PARA ENVIO
server.login(endmail,pswd)
try: 
#cria uma variavel com o corpo da mensagem
    message = ('Variavel responsavel pelo armazenamento da mensagem')
    server.sendmail(endmail, from_mail ,message)
    print("Mensagem enviada com sucesso") 
# Caso haja queda na conexao de email, realize o login novamente    
except smtplib.SMTPServerDisconnected:
    print("Erro de conexao SMTPServerDisconnected")
    server.starttls()
    server.ehlo()
    server.login(endmail,pswd)     
```

  Para instalar o módulo digite:<br>
  ```  $ pip install smtp   ```

</details>
<details>
  <summary> BRICANDO COM STRINGS</summary><br>
  <details>
<summary>    Letreiro de LED</summary><br>
Esse código "simula" um letreiro de led.

![](Codigo_Python/Letreiro/letreiro.gif)

```python
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from os import system #
from time import sleep #

# Texto de Exemplo

texto = "Python é uma linguagem de programação de alto nível,[4] interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.[1] Atualmente possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem como um todo não é formalmente especificada. O padrão de facto é a implementação CPython. A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional. Prioriza a legibilidade do código sobre a velocidade ou expressividade. Combina uma sintaxe concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros. "

comeco = 0
fim = 30
while fim < len(texto): # Enquanto o "fim" for menor que o tamanho total do texto, faca:
	comeco += 1 # Adciona um ao começo
	fim += 1    # Adciona um ao fim
	system('clear') # Limpa a tela (Funciona melhor em um terminal)
	sleep(0.2) # Espera 0,2 segundos
	print("|{}|".format(texto[comeco:fim])) # printa o texto da variavel "comeco" a variavel "fim"
  ```
  </details>
</details>



<details>
  <summary> CREATE FAKE</summary><br>

### Esse programa tem como objetivo realizar a criação de dados falsos, a partir dos dados de criação de uma tabela.

Para utilizar o programa você deverá ter um arquivo contendo informações sobre a tabela.

As informações deverão estar da seguinte maneira:
```
Nome_da_Coluna Tipo_do_Campo(Quantidade),
Nome_da_Coluna2 Tipo_do_Campo2.
```

```
id_num INTEGER,
nm VARCHAR(20),
bl_id DECIMAL(20,4)
```

Deverá conter o nome do campo, um espaço entre o nome do campo e o tipo do campo, e caso precise o tamanho do campo. Para finalizar uma virgula no final.<br>
Lembrando que o codigo só irá processar os dados com o tipo INTEGER, VARCHAR, DATE e DECIMAL. Caso precise que ele processe algum tipo de dado diferente dos citados, crie uma função onde será realizado criação de dados aleatórios de sua preferencia, e coloque a chamada na função "grava_insert", adcionando a um dos "IFs".

Dessa forma o programa poderá ler e criar dados aleatórios, sendo preciso apenas indicar o caminho do arquivo de leitura e a quantidade de linhas que deseja formar os dados. Assim você poderá testar qualquer tabela com dados inseridos, sem precisar criar os famosos "teste01", "teste". 


```python
# MODULOS
from time import gmtime, strftime
from random import uniform
from random import randint
from random import choice
import string

# LISTAS
lista_tipos = []
lista_numero = []

# TIPOS DE DADOS
def VARCHAR(data_qt):
    lista_de_letras = string.ascii_lowercase
    nome = []
    letters = string.ascii_lowercase
    nome =  (''.join(choice(letters) for i in range(0,int(data_qt))))
    return("'{}'".format(nome[0].upper()+nome[1:]))

def DECIMAL(data_qt):
    return(round(random.uniform(0,int(data_qt[0])), int(data_qt[1])))

def INTEGER():
    return(randint(0,100))

def DATE():
    data = strftime("%Y-%m-%d", gmtime())
    return("'{}'".format(data))

# FUNCAO QUE REALIZA LEITURA DA TABELA
def leitura_dados():
    with open(arquivo,"r") as file:
        print(30*"~^")
        print("\nLENDO ARQUIVO\n")
        print(30*"~^")
        for f in file:
            f = f.split(" ")
            nm_coluna = f[0]
            nm_tipo = f[1]
            try:
                nm_tipo = f[1].split("(")
                data_type = str(nm_tipo[0])
                data_qt = str(nm_tipo[1]).replace(")","")
            except:
                data_qt = 0
                pass
            lista_tipos.append((data_type.lower()).replace(",\n",""))
            try:
                data_qt = int(data_qt.replace(",\n",""))
            except:
                pass
            lista_numero.append(data_qt)
    grava_insert()

# FUNCAO QUE REALIZA A GRAVACAO DOS DADOS ALEATORIOS
def grava_insert():
    lista_de_dados = []
    print(30*"~^")
    print("\nGRAVANDO ARQUIVO\n")
    print(30*"~^")
    for indice in range(0,num_max):    
        with open(nome_table+".csv","a") as file_write:
            for c in range(len(lista_tipos)):
                if lista_tipos[c] in "decimal":
                    dados = DECIMAL(lista_numero[c])
                elif lista_tipos[c] in "varchar":
                    dados = VARCHAR(lista_numero[c])
                elif lista_tipos[c] in "integer":
                    dados = INTEGER()
                elif lista_tipos[c] in "date":
                    dados = DATE()
                else:
                    print("TIPO NÃO ENCONTRADO")
                file_write.write(str(dados))
                if c+1 != len(lista_tipos):
                    file_write.write(",")
            file_write.write("\n")
    print(30*"~^")
    print("\nTHAT'S ALL FOLKS!!!\n")
    print(30*"~^")

# INPUTS
arquivo = str(input("Digite o caminho do arquivo: "))
nome_table = str(input("Digite o Nome da Tabela: "))
num_max = int(input("Quantidade de Linhas: "))

# RUN
leitura_dados()
            
```

</details>
	  
	  





