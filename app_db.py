from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Dados do DB: 
# Cadastro de Pessoa - Identificador (número inteiro aleatório único), Nome da pessoa, Idade (número inteiro)
# Cadastro de transação -  Identificador (número inteiro aleatório único), Descrição (Texto), Valor (Número decimal positivo), Tipo (Despesa/Receita), Pessoa (inteiro identificador da pessoa do cadastro anterior)
# Lembrando que Pessoa no cadastro de transação é o mesmo identificador do cadastro de pessoa
# O banco de dados será composto de um número identificador aleatório gerado pelo computador
# Será um único banco de dados composto de identificador 

# Modelo login de usuário
class User(db.Model):
    __tablename__ = 'usuarios'
    id_user = db.Column(db.Integer, primary_key=True)
    nome_de_usuario = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    
# Modelo Pessoa
class Pessoa(db.Model):
    __tablename__ = 'pessoas'  # Nome da tabela no banco de dados
    id_pessoa = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Id da pessoa (auto incremento)
    nome = db.Column(db.String(100), nullable=False)  # Nome da pessoa (não pode ser nulo)
    idade = db.Column(db.Integer, nullable=False)  # Idade da pessoa (não pode ser nulo)
    id_user = db.Column(db.Integer, db.ForeignKey('usuarios.id_user'), nullable=False)

    # Relacionamento com a tabela Transacao
    transacoes = db.relationship('Transacao', backref='pessoa', lazy=True, cascade='all, delete-orphan')  # Define o relacionamento com a tabela Transacao

    def __repr__(self):
        return f'<Pessoa {self.nome}>'

# Modelo Transacao
class Transacao(db.Model):
    __tablename__ = 'transacoes'  # Nome da tabela no banco de dados
    id_transacao = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Id da transação (auto incremento)
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoas.id_pessoa'), nullable=False)  # Referência à pessoa
    descricao = db.Column(db.Text)  # Descrição da transação
    valor = db.Column(db.Numeric(10, 2), nullable=False)  # Valor da transação (número decimal)
    tipo = db.Column(db.String(50), nullable=False)  # Tipo da transação (Despesa ou Receita)

    # Garantia de que só pode ser 'Despesa' ou 'Receita'
    __table_args__ = (
        db.CheckConstraint("tipo IN ('Despesa', 'Receita')", name="tipo_check"),
    )

    def __repr__(self):
        return f'<Transacao {self.id_transacao}>'