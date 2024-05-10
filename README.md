# Buscas Heurísticas

## Otimização de rota entre Arad e Bucharest: Escolher menor rota entre os destinos utilizando as buscas heurísticas (Gulosa e A*)


* Código desenvolvido para a disciplina de Inteligência Artificial - ECOI19, cursada na Universidade Federal de Itajubá - _Campus_ Itabira

* Problemática do trabalho:
    * Selecionar a rota com menor custo para ir da origem até o destino definido (Arad > Bucharest) , com base na malha rodoviária das cidades da Romênia.
    * Verificar qual dos trajetos tem maior complexidade, completude e otimalidade, além de fornecer o caminho mais otimizado , visando os pontos que percorreu, as milhas percorridas e os pontos verificados para a escolha do caminho.
    * Desenvolver a implementação utilizando os dois diferentes métodos de busca definidos pelo docente ( Busca Gulosa e Busca A*)

### Malha rodoviária das cidades da Romênia

<img src="RoteiraSimplificado.png" alt="Malha rodoviária das cidades da Romênia" width="500" height="300">

### Distância de cada uma das cidades até o destino proposto (Bucharest)

<img src="ListadeCidades.png" alt="Distância de cada uma das cidades até o destino proposto (Bucharest)" width="500" height="190">

### Comparativo resumido dos algoritmos de busca definidos, levando em cotna a completude, complexidade e otimalidade de cada método

<img src="Comparativo (1).png" alt="Comparativo dos métodos de busca utilizados" width="650" height="300">

### Resultado da implementação 

<img src="ResultadoAlgoritmo.png" alt=" Resultado da implementação" width="500" height="150">

### Caminho Percorrido - Busca A* (A estrela)

<img src="Diagrama-Aestrela.drawio.png" alt="Ilustração do caminho percorrido pela busca A estrela, de acordo com o algoritmo implementado." width="550" height="650">


### Caminho Percorrido - Busca Gulosa

<img src="Diagrama-gulosa.drawio.png" alt="Ilustração do caminho percorrido pela busca gulosa, de acordo com o algoritmo implementado." width="370" height="600">