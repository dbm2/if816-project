# if816-project

**Autor:** Daniel Barbosa Maranhão | 107.698.344-85
**Login: ** dbm2 
**Data:** 18/10/2018

### Descrição
Projeto de métodos númericos que recebe como entrada um arquivo com métodos a serem calculados e gera um arquivo de saída com as respectivas respostas.

### Biblíotecas
mpmath, sympy e matplotlib.

### Sistema Operacional
O programa foi desenvolvido no Windows 10 e testado apenas nele. Qualquer problema me fala!!

### Preparação
Para poder executar o programa é necessário instalar as bibliotecas utilizadas.
Para isso, navege pelo terminal até a pasta em que o projeto está e execute o seguinte comando: 
```sh
$ pip install -r requirements.txt
```

### Execução
Para executar o programa, navege pelo terminal até a pasta em que o projeto está e execute o seguinte comando:
```sh
$ python -u project.py
```

### Entrada
O arquivo de entrada com os métodos que serão calculados ficam em "/resources/entrada.txt".
Como foi especificado, os métodos de entrada sempre seguirão um dos seguintes padrões abaixo:
  - nome_do_metodo y0 t0 h passos função
  - nome_do_metodo y's t0 h passos função ordem
  - nome_do_metodo y0 t0 h passos função ordem

Exemplos de entradas válidas:
  - euler 0 0 0.1 20 1-t+4*y
  - adam_bashforth 0.0 0.1 0.23 0.402 0.6328 0 0.1 20 1-t+4*y 5
  - adam_multon_by_euler_aprimorado 0 0 0.1 20 1-t+4*y 6
  - formula_inversa_by_runge_kutta 0 0 0.1 20 1-t+4*y 6

Observação: eu deixei o arquivo de entrada com todos os métodos exemplos da especificação. Pode executar assim se desejar.

### Saída
As respostas dos métodos de entrada serão gravadas no arquivo "/resources/saida.txt" seguindo o padrão especificado.
Além disso, os gráficos para os métodos serão gerados dentro da pasta "/resources/charts". Serão gerados tanto gráficos individuais (seguindo o padrão de nome "chart_nome_do_metodo.png") quanto um gráfico geral com todos métodos (com o nome "chart_all.png")

Exemplo de saída:
> Metodo de Euler <br/>
> y(0.0) = 0.0 <br/>
> h = 0.1 <br/>
> 1 0.1 <br/>
> 2 0.22999999999999998 <br/>
> 3 0.402 <br/>
> 4 0.6328 <br/>
> 5 0.9459200000000001 <br/>
> 6 1.3742880000000002 <br/>
> 7 1.9640032000000003 <br/>
> 8 2.7796044800000006 <br/>
> 9 3.911446272000001 <br/>
> 10 5.486024780800001 <br/>
> 11 7.680434693120002 <br/>
> 12 10.742608570368002 <br/>
> 13 15.019651998515204 <br/>
> 14 20.99751279792129 <br/>
> 15 29.356517917089803 <br/>
> 16 41.04912508392572 <br/>
> 17 57.40877511749601 <br/>
> 18 80.30228516449442 <br/>
> 19 112.34319923029219 <br/>
> 20 157.19047892240906b <br/>