###Esse programa tem como objetivo realizar a criação de dados falsos, a partir dos dados de criação de uma tabela.

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

Deverá conter o nome do campo, um espaço entre o nome do campo e o tipo do campo, e caso precise o tamanho do campo. Para finalizar uma virgula no final.

Dessa forma o programa poderá ler e criar dados aleatórios, sendo preciso apenas indicar o caminho do arquivo de leitura e a quantidade de linhas que deseja formar os dados. Assim você poderá testar qualquer tabela com dados inseridos, sem precisar criar os famosos "teste01", "teste". 


