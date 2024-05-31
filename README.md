# Documentação do Projeto: Calculus Jenga
###  Objetivo
O projeto "Calculus Jenga" tem como objetivo principal reforçar os conceitos de cálculo multivariável de forma interativa e divertida. Utilizando a metáfora do jogo Jenga, os alunos são desafiados a responder perguntas sobre derivadas parciais, pontos máximos e mínimos, e integral dupla. A cada resposta correta, um bloco é adicionado à torre Jenga virtual, e a cada erro, um bloco é removido. O jogo termina quando a torre chega ao fim, quando ela chega ao topo ou quando todas as perguntas são respondidas.

Implementação
O jogo foi desenvolvido utilizando a linguagem Python e a biblioteca Pygame, escolhidas por sua facilidade de uso, compatibilidade e recursos gráficos. O projeto segue a abordagem de implementação em código, criando um "serious game" que combina elementos de entretenimento com aprendizado.

Tema
O tema central do jogo gira em torno dos seguintes conceitos de cálculo multivariável:

Derivadas Parciais: O jogo apresenta questões que exigem o cálculo de derivadas parciais de funções de múltiplas variáveis.
Cálculo de Ponto Máximo e Mínimo: Os jogadores precisam identificar pontos críticos e determinar se são máximos ou mínimos
Integral Dupla: O jogo inclui questões relacionados ao cálculo de integrais duplas sobre regiões específicas.

## Concepção e Design
O Calculus Jenga foi projetado para estudantes de cálculo que buscam encontrar questões para se desafiar, praticar e consolidar seus conhecimentos.

### A mecânica do jogo envolve:

#### Escolha da Dificuldade: 

O jogador pode selecionar entre três níveis de dificuldade (Fácil, Médio, Difícil), que alteram o tempo limite para responder cada pergunta.
#### Número de Perguntas:
O jogador também pode escolher o número de perguntas que deseja responder.
#### Respostas e Feedback: 
As perguntas são exibidas na tela, e o jogador insere a resposta usando o teclado. O jogo fornece feedback imediato sobre a correção da resposta.
#### Construção e Desconstrução da Torre: 
A cada resposta correta, um bloco é adicionado ao topo da torre. A cada erro, um bloco é removido. 

#### Fim do Jogo: 

O jogo termina quando a torre cai (respostas erradas demais) ou quando todas as perguntas são respondidas (vitória). 

### Desafios de Programação

Durante o desenvolvimento, os principais desafios enfrentados foram:

#### Geração de Perguntas: 

Foi necessário criar um sistema para gerar perguntas aleatórias sobre os conceitos de cálculo multivariável, garantindo a variedade e o nível de dificuldade adequado.

#### Lógica do Jogo: 
A implementação da lógica da torre Jenga, incluindo a adição e remoção de blocos, exigiu atenção aos detalhes para evitar erros.

#### Controle de Tempo: 
O jogo possui um cronômetro para cada pergunta, o que demandou a utilização de funções de tempo e a sincronização com a interface do usuário.
#### Tratamento de Erros: 
Foi necessário implementar mecanismos para lidar com erros de entrada do usuário, como respostas inválidas ou estouro do tempo.
### Fluxo do Jogo
#### Menu Inicial: 
O jogador é recebido com um menu de boas-vindas.
#### Escolha da Dificuldade: 
O jogador seleciona o nível de dificuldade desejado.
#### Número de Perguntas: 
O jogador informa quantas perguntas deseja responder.
#### Jogo Principal: 
As perguntas são apresentadas sequencialmente, com um cronômetro.
#### Feedback e Atualização da Torre: 
O jogo fornece feedback sobre as respostas e adiciona ou remove blocos da torre.
#### Fim do Jogo: 
O jogo termina com a vitória (todas as perguntas respondidas) ou derrota (torre cai). O resultado é exibido, juntamente com as perguntas utilizadas na partida.
### Feedback e Iteração
O jogo foi testado com colegas e futuros usuários, e o feedback recebido foi fundamental para aprimorar a jogabilidade, a interface e a qualidade das perguntas.

### Conclusão
O Calculus Jenga é um projeto que une a diversão do jogo à prática do cálculo multivariável. Ao combinar elementos visuais, desafios interativos e feedback imediato, o jogo proporciona uma experiência de aprendizado mais engajadora e eficaz.

### Tecnologias Utilizadas
Linguagem de Programação: Python

Biblioteca Gráfica: Pygame
### Próximos Passos
#### Aprimoramento das Perguntas: 
Adicionar mais perguntas e variar os tipos de questões para abranger uma gama mais ampla de conceitos de cálculo multivariável.
#### Melhorias na Interface: 
Tornar a interface mais intuitiva e visualmente atraente, com gráficos e animações mais elaboradas.
#### Recursos Adicionais: 
Implementar um sistema de dicas, tutoriais interativos ou um modo de prática para auxiliar o aprendizado.
### Considerações Finais
O Calculus Jenga é um projeto em constante desenvolvimento, com potencial para se tornar uma ferramenta valiosa no ensino e aprendizado do cálculo multivariável. Agradecemos o feedback e as sugestões para futuras melhorias.