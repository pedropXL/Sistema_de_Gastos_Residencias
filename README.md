# **Sistema de Gastos Residênciais**
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
[![Static Badge](https://img.shields.io/badge/LinkedIn-www.linkedin.com%2Fin%2Fpedropedrazzi-blue)](https://www.linkedin.com/in/pedropedrazzi)

## Visão Geral do Projeto
Este é um sistema de gerenciamento de gastos residenciais que permite o cadastro de pessoas, a inserção de transações financeiras (despesas e receitas) para cada pessoa e a visualização do total por pessoa e o total geral. O sistema foi desenvolvido utilizando Flask, PostgreSQL, HTML, CSS e JavaScript.


## **Tabela de Conteúdos**

- [Características e Funcionalidades do Sistema](#características-e-funcionalidades-do-sistema)
- [Requisitos](#requisitos)
- [Como Executar o Sistema](#como-executar-o-sistema)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Modelo de Banco de Dados](#modelo-de-banco-de-dados)
- [Calculo dos Totais](#calculo-dos-totais)
- [Front-End](#front-end)

## **Características e Funcionalidades do Sistema**

- **Cadastro de Pessoas**: O sistema permite que o usuário cadastre pessoas a partir do Nome e da Idade delas. O sistema cria o cadastro a partir do Nome e da Idade da pessoa, registra no Banco de Dados e gera um id(um número sequencial único) que fica registrado no banco de dados mas não é impresso na interface. O sitema também impede números de serem digitados no nome e permite apenas números inteiros positivos de serem inseridos como idade. Além disso, qualquer nome independentemente de como for escrito é registrado apenas com as primeiras letra de cada palavra como maiúsculo. Cada fileira da tabela contém todas as informações da transação:

Em seguida, cada pessoa ficará listada na interface por meio de uma tabela feita com um Design "Clean". Cada fileira da tabela contém todas as informações da pessoa: Nome e Idade; menos o id da pessoa que apenas é registrado internamente no Banco de Dados.

O usuário pode deletar o cadastro de qualquer pessoa, ao deletar o cadastro de uma pessoa todas as suas transações são deletadas.

- **Cadastro de Transações**: O sistema permite que o usuário cadastre transações para cada pessoa cadastrada. Para cadastrar as transanções o usuário precisa digitar a Descrição da transação, digitar o valor da transação (em números decimais positivos), selecionar o tipo da transação, Despesa ou Receita, a partir de um seletor visual e selecionar a pessoa que fez a transação a partir de um seletor visual. Toda vez que o usuário registra uma transação é enviado para Banco de Dados e um id(um número sequencial único) é gerado para autentificar e diferenciar cada transação. 

Após registar as transações, elas ficaram listadas na interface por meio em uma tabela feita com um Design "Clean". Cada fileira da tabela contém todas as informações da transação: Descrição, Valor, Tipo e Pessoa; menos o id da transação que apenas é registrado internamente no Banco de Dados.

O usuário apenas pode inserir transações do tipo Receita para pessoas com mais de 18 anos de idade, caso o usuário tente inserir transações do tipo Receita para pessoas com menos de 18 anos idade o sistema retornará um erro demonstrado na interface.

- **Total por Pessoa**: Calcula o Total de Receitas, o Total de Despesas e o Saldo Líquido(Total de Receitas - Total de Despesas) e exibe em uma interface por meio de uma tabela em que cada fileira corresponde a pessoa (com seu nome sendo mostrado na fileira) e o Total de Receitas, o Total de Despesas e o Saldo Líquido dela.

- **Total Geral**: Calcula o Total de Receitas Geral (a soma do Total de Receitas de todas as pessoas), o Total de Despesas Geral (a soma do Total de Despesas de todas as pessoas) e o Saldo Líquido Geral (Total de Receitas Geral - Total de Despesas Geral). Todos esses dados são impressos por meio de uma tabela com uma única fileira com esses dados.

## **Requisitos**

- Python 3.x;
- Flask;
- Flask-SQLAlchemy;
- PostgreSQL;
- Psycopg2;

## **Como Executar o Sistema**

1. Instale as dependências do Python:

    No diretório do projeto, crie e ative um ambiente virtual.

    Para isso digite no terminal os seguintes comandos: 
    `python -m venv venv`
    `source venv/bin/activate  # No Windows, use venv\Scripts\activate`

    Depois selecione o Ambiente Virtual como interpretador, caso estiver usando o Visual Studio Code será:

    - Acesse a paleta de comando (pressione `Ctrl + Shift + P`);
    - Digite `Python: Select Interpreter` e selecione o interpretador do ambiente virtual que você criou (ele geralmente aparece como `./venv/bin/python` ou `.\venv\Scripts\python.exe` no Windows).

2. Instale as dependências:

    - Digite no terminal: `pip install flask flask-sqlalchemy psycopg2`

3. Configuração do Banco de Dados PostgreSQL:

    Crie um banco de dados PostgreSQL com o nome db_app ou altere a configuração de banco de dados no arquivo app.py para refletir o nome e as credenciais do seu banco de dados.

    Certifique-se de que o PostgreSQL esteja rodando no seu sistema. A URI de conexão com o banco é definida como:

    - `app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:senha@localhost:5432/db_app'`

    Substitua o caminho para o banco de dados dentro do código fonte pelo caminho do seu banco de dados.
    
    Obs: No código fonte foi usado um método para proteger as credenciais do banco de dados, no caso foi utilizado a biblioteca dotenv e usado um .gitignore para não exibir as credenciais. Por isso você não precisa da biblioteca dotenv ou usar o .gitnore, você pode apenas substituir `app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'` pelo método logo acima escrevendo com as credenciais do seu banco de dados. Mas caso for fazer uma branch do projeto ou clonar o projeto e decidir disponibiza-lo open-source é altamente recomendável omitir as credenciais do seu banco de dados para que não ocorra invasões ou vazamento de dados indesejados. 

    - Criação das Tabelas no Banco de Dados:

    Para a criação das tabelas no banco de dados escreva o seguinte código após a URI de conexão:

    `#@app.route('/')`
    `#def criar_tabelas():`
        `#db.create_all()  # Cria todas as tabelas definidas no modelo`
        `#return "Tabelas criadas com sucesso!"`

    Isso criará as tabelas do banco de dados ao acessar a URL raiz.

    Caso você veja escrito no terminal "Tabelas criadas com sucesso!" então as tabelas foram criadas ou você acessar o banco de dados e verificar se as tabelas foram criadas.

    Ao rodar a aplicação pela primeira vez, as tabelas necessárias serão criadas automaticamente.

    Após isso elimine o código de criação de tabelas no banco de dados ou torne ele um comentário para que código não crie outra tabela ou retorne um erro.

4. Como Executar o sistema:

    Rodando o Sistema:

    - No diretório do projeto, execute o seguinte comando para rodar o servidor Flask:
    
      flask run

      ou

      python app.py

      A aplicação estará disponível em http://127.0.0.1:5000/.

## **Estrutura do Projeto**

/
├── app.py              # Arquivo principal do Flask
├── app_db.py           # Modelos de banco de dados
├── templates/          # Contém os templates HTML
│   ├── cadastro_de_pessoa.html
│   ├── cadastro_de_transacoes.html
│   ├── totais_gerais.html
│   └── totais_por_pessoa.html
├── static/             # Arquivos estáticos (CSS, JS, imagens)
│   ├── style.css
└── venv/               # Ambiente virtual Python

## **Modelo de Banco de Dados**

O banco de dados é composto por duas tabelas principais:

Pessoa: Armazena informações de cada pessoa (ID, nome, idade).
Transacao: Armazena informações sobre as transações financeiras (ID, descrição, valor, tipo, e o ID da pessoa associada).

As transações podem ser classificadas como "Despesa" ou "Receita". O sistema valida que apenas pessoas maiores de 18 anos podem cadastrar receitas.

## **Calculo dos Totais**

O sistema calcula os totais de receitas, despesas e saldo líquido utilizando consultas ao banco de dados. Para cada pessoa, o total de receitas e despesas é somado, e o saldo líquido é a diferença entre as receitas e as despesas.

## **Front-End**

O sistema utiliza templates HTML e CSS "linkado" ao HTML base para exibir as informações. A interface foi desenvolvida com base em um Design "Clean" ou "Limpo" marcado pela simplicidade, funcionalidadem, com cores claras e suaves, com o uso de elementos com bordas suaves e redondas, navegação intuitiva e hierarquia entre as estruturas. 

É possível navegar entre as diferentes páginas, URLs, do projeto por meio do cabeçado principal. O arquivo "base.html" é usado para reutilizar o código para os outros arquivos de template HTML, assim torna o código mais eficiente e evita a redundância. O uso de JavaScript nas páginas permite manipular dinamicamente a exibição das transações, como a mudança de cor para "Despesa" (vermelho) e "Receita" (verde), imprimir números decimais apenas com vírgulas e permitir que apenas letras sejam digitadas no campo de Nome.

## **Contribuição**

As contribuições são bem-vindas! Se quiseres contribuir, por favor bifurca o repositório e submete um pull request com as tuas alterações. Sinta-se livre para melhorar o projeto, tornar o código mais eficiente, corrigir possíveis bugs e adicionar mais funcionalidades.

---

## **Licença**
Este projeto está licenciado sob a licença MIT. Veja o ficheiro LICENSE para mais detalhes.

---

## **Links**

[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pedropedrazzi)

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pedropXL)

## **Contacto e Feedback**

Para quaisquer questões ou feedback, por favor abra um problema no GitHub ou contacte o responsável pelo projeto.

Email para contacto: pedroppedrazzi@gmail.com
