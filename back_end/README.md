## Requisitos  
- Python 3 - https://www.python.org/  
- Flask - `pip3 install Flask`  
- SQLAlchemy - `pip3 install SQLAlchemy`  
- Flask SQLAlchemy - `pip3 install Flask-SQLAlchemy`  
- Flask CORS - `pip3 install flask-cors`  
- Flask Testing - `pip3 install Flask-Testing`  

Dúvidas referente as versões consulte o arquivo `requirements.txt`.  
Não foi utilizado um gerenciador de variáveis de ambiente como `dotenv` neste caso para alterar as configurações como `porta` e `host` edite o arquivo `config.py`  
**Obs.:** Na pasta `db` existe o arquivo `basic_data.sql` que possui alguns registros para teste.  
## Iniciando aplicação
- Para iniciar a aplicação execute no terminal/prompt de comando o comando `python app.py`, certifique-se de esta no root (diretório principal) da aplicação e que as variáveis de ambiente do sistema operacional estão configuradas para executar na versão 3 do Python. Para acessar a aplicação basta utilizar as informações configuradas no `config.py`. Ex.: http://localhost:8080  

## Consumindo API

**Estudantes**  
Lista todos os estudantes cadastrados
- Métodos de requisição: GET
- Rota: /students
- Parâmetros: N/A
- Content-Type: *
- CURL: curl http://localhost:8080/students

Cadastrar novo estudante
- Métodos de requisição: POST
- Rota /students
- Parâmetros: String: name
- Content-Type: application/json
- CURL: curl -X POST -H 'Content-Type: application/json' -d '{"name":"Pedro"}' http://localhost:8080/students

**Disciplinas**  
Lista todos as disciplinas cadastradas
- Métodos de requisição: GET
- Rota: /subjects
- Parâmetros: N/A
- Content-Type: *
- CURL: curl http://localhost:8080/subjects

Cadastrar novo disciplina
- Métodos de requisição: POST
- Rota /subjects
- Parâmetros: String: name
- Content-Type: application/json
- CURL: curl -X POST -H 'Content-Type: application/json' -d '{"name":"Física"}' http://localhost:8080/subjects

**Aluno na disciplina**  
Lista alunos cadastrados na disciplina
- Métodos de requisição: GET
- Rota: /students_subjects/subject_id
- Parâmetros: N/A
- Content-Type: *
- CURL: curl http://localhost:8080/students_subjects/1

Cadastra aluno na disciplina
- Métodos de requisição: POST
- Rota /students_subjects/subject_id
- Parâmetros: Integer: student
- Content-Type: application/json
- CURL: curl -X POST -H 'Content-Type: application/json' -d '{"student": 1}' http://localhost:8080/students_subjects/1

**Presença**  
Lista alunos com ou sem presença com base no dia
- Métodos de requisição: GET
- Rota: /attendances/subject_id/date
- Parâmetros: N/A
- Content-Type: *
- CURL: curl localhost:8080/attendances/1/2020-04-12
-
Registra presença para o aluno
- Métodos de requisição: POST
- Rota /attendances/subject_id/date
- Parâmetros: Boolean: attendance, Integer: student
- Content-Type: application/json
- CURL: curl -X POST -H 'Content-Type: application/json' -d '{"attendance": true, "student": 1}' curl localhost:8080/attendances/1/2020-04-12