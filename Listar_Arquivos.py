import glob
listar_arquivo = glob.glob('*.*')# PROCURA NO DIRETORIO TODO ARQUIVO QUE TENHA EXTENSÃO "xlsx".
with open("Lista_Nome_Arquivos.txt","w") as f:
    for linha in listar_arquivo:
        f.write(linha+"\n")