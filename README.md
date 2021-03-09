# Gerenciador de Tarefas
 
**Número da Lista**: 1<br>
**Conteúdo da Disciplina**: Grafos 2<br>
 
## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0122549 |  Paulo Gonçalves Lima |
| 17/0113060 |  Pedro Vítor de Salles Cella |
 
## Sobre
<p1>A nossa ideia inicial era criar um gerenciador de tarefas, onde a pessoa colocava as tarefas, quanto cada tipo de tarefa deve ser concluída no dia e o peso de cada tipo de tarefa para o dia, o programa utilizando o algoritmo de Dijkstra descobriria o caminho mais otimizado para esse conjunto de tarefas.</p1>
 
## Propriedades impostas no problema:
 - É um grafo que representa o passar do tempo, cada linha dele significa que se passou X tempo.
 - Cada atividade tem um peso diferente dependendo da atividade que foi feita anteriormente, então cada atividade feita pode escolher qualquer uma das outras atividades cadastradas.
 - Sempre começa com o node de acordar e termina com o node de dormir <br>
 - Um dia sempre é das 6 horas da manhã até as 22 horas.
![Representação do grafo](/docs/RepresentacaoGrafo.png)
- Com essas propriedades o grafo que é gerado acaba sendo uma árvore, onde nenhum node tem como ser um node já visitado a não ser o último node que é o node de convergência entre todos os outros nodes gerados.
- As tarefas são ditadas por 2 funções a primeira dita a vontade de se fazer qualquer tipo de trabalho onde quanto maior menos a chance dele ser escolhido:
![Tarefas Grafico](/docs/tasks.png)
<br>
 
 - Independentemente das tarefas que a pessoa coloque sempre teremos uma tarefa de comer para que simule a vontade da pessoa comer durante o dia, que essa tarefa é controlada por uma função diferente das tarefas:
![Comer Grafico](/docs/comer.png)

Juntando os 2 graficos temos:
![2Grafos](/docs/Funcoes.png)
Onde temos apenas 1 ponto de encontro entre as 2 que é no momento que o node de comer tem a maior chance de ser escolhido.
### Problemas:
 
<p1>Como o grafo gerado foi uma árvore, nós não poderíamos ter muitas instâncias de tempo passando pois caso uma pessoa coloque que tem que fazer 5 tarefas no dia e caso a gente decida dividir para passar o tempo de 1 em 1 minuto isso quer dizer que o dijkstra pode escolher uma nova tarefa todo minuto teríamos um total de 5^(960) nodes, por essa razão adotamos 2 estratégias para diminuir esse numero:</p1>
1. Diminuir o tempo que se pode fazer a decisão então de 960 escolhemos 150 o que quer dizer que cada escolha de node representa um tempo de 6,4 minutos.
2. Durante a fase da lista de prioridades pegamos apenas as primeiras 500 melhores escolhas, e desistimos do resto.
   
Por causa da segunda estratégia que escolhemos, não podemos dizer com a certeza que o caminho escolhido é o melhor caminho, mas ele é um dos melhores, se não o melhor, mas não podemos ter a certeza por jogarmos fora algumas escolhas.
 
Mesmo com as 2 estratégias o total de nodes gerados no exemplo acima foi de 427562 nodes.
<br>
<br>
OBS:. Caso você queira alterar essas propriedades de quanto tempo cada escolha representa e quanto jogamos fora da lista de prioridades os 2 estão nas linhas 85 do arquivo Dijkstra e na linha 50 do arquivo Demo respectivamente
 
 
## Screenshots
![Screenshot2](./docs)
![Screenshot3](./docs)
 
## Instalação 
**Linguagem**: Python<br>
 
<p>Para usar nosso projeto primeiro deve-se ter instalado o Python3 e uma biblioteca do Python chamada prettytable, siga as etapas:</p>
 
<p>Caso não tenha o Python3 instalado:</p>
 
```
sudo apt-get install python3
```
 
<p>Para instalar a biblioteca é bem simples, basta baixar pelo Linux ou baixar usando o pip</p>
 
Linux<br>
```
sudo apt-get install -y python3-prettytable
```
 
Pip<br>
```
python -m pip install -U prettytable
```
 
**OBS:** Nós não conseguimos instalar pelo pip, por isso deixamos a opção do Linux caso passe pelo mesmo problema
 
## Uso 
Explique como usar seu projeto caso haja algum passo a passo após o comando de execução.
 
## Outros 
<p>Aqui se encontra o vídeo explicativo do projeto, <a id="video-explicativo" href="">baixe</a> ou veja-o online <a id="video-explicativo" href="">aqui</a></p>
 
 
 
 
 
 
 

