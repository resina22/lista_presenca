**Requisitos**

NodeJS >= v12.16.*  
Para configurar qual API o react vai consumir altere a variável *REACT_APP_API* no arquivo *.env*  

 **Instalação**  
- Execute o no terminal/promp de comando o comando `npm install` no root (pasta principal) do projeto  
- Para iniciar a aplicação execute no terminal/promp de comando o comando `npm start`, o evento padrão é após o carregamento abrir o navegador com a aplicação, mas se não ocorrer basta acessar http://localhost:3000/  

**Funcionalidades**  
- Na tela inicial deve ser listada todas as disciplinas cadastradas, para realizar o lançamento de presença basta escolher a data e clicar sobre a disciplina  
**Obs.:** Aluno, Disciplina, Status de presença e alunos na disciplina já devem estar previamente cadastrados.  

- Na tela de lançamento de notas é possível buscar pelo nome do aluno e lançar presença ou remover a mesma, os alunos que possuem a linha Pendente na frente do nome ainda não foram definidos como Presente ou Ausente