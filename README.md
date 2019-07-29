# Tools
Scripts curtos, e úteis.

<details>
  <summary> Listar Arquivos </summary><br>

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
  <summary>Envio de E-mail (smtplib)</summary><br>
  
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
