import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

with open("Log.txt","w+") as log:
    print("LIMPANDO ARQUIVO DE LOG")

dic = {}

#Define email e senha de envio
sender_address = 'E-mail para envio'
sender_pass = '************'

# Define message['From'] como o email de envio. 
message = MIMEMultipart()
message['From'] = sender_address

# Realiza leitura de arquivo com contatos
def contatos():
    print(20*"-")
    print("Lendo Arquivo 'contatos.csv'")
    print(20*"-")
    with open("contatos.csv","r") as contatos:
        for itens_contato in contatos:
            itens_contato = itens_contato.split("|")
            pessoa = itens_contato[0]
            email = itens_contato[1]
            dic[pessoa] = email
            print(pessoa,email)


# Para cada nome e contato de email no dicionario "dic", chamar funcao enviar_email() passando os paramentros de nome(value) e email(key)
def processo():
    for key, value in dic.items():
        enviar_email(value,key)


# Realiza o envio dos e-mails, de acordo com arquivos disponiveis na pasta, e o nome do funcionario disponivel no dicionario
def enviar_email(receiver_address,key):
    mail_content = ('''OLÁ '''+key+'''.
SEGUE EM ANEXO O HOLERITE.
''')
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = ('Holerite {}.'.format(key))
    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = ('{}.pdf'.format(key))
    # Caso o arquivo exista na pasta, enviar o arquivo
    with open("Log.txt","a") as log:
        try:
            attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload) #encode the attachment
            #add payload header with filename
            # payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
            payload.add_header('Content-Disposition', "attachment; filename= {}".format(attach_file_name))
            message.attach(payload)
            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            print('Mail Sent')
            print(key,receiver_address)
            log.write("ARQUIVO ENVIADO COM SUCESSO | Nome: {} | E-Mail: {}\n".format(key,attach_file_name))
        # Caso nao ache o arquivo, devolver mensagem de erro, informando qual e-mail nao foi enviado
        except FileNotFoundError:
            print(35*"~-")
            print("O ARQUIVO {} NAO FOI ENCONTRADO".format(attach_file_name))
            print(35*"~-")
            log.write(" ^-^-^-^ O ARQUIVO {} NAO FOI ENCONTRADO ^-^-^-^\n".format(attach_file_name))


n = input(str("Tecle [S] para continuar:"))
if n.upper() == 'S':
    contatos()
    processo()
