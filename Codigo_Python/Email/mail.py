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
