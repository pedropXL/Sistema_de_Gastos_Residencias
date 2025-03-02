from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import func
from app_db import db, Pessoa, Transacao  # Importando db e os modelos de app_db.py
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Carregar as variáveis do arquivo .env
load_dotenv()

# Obter as credenciais do banco de dados das variáveis de ambiente
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desabilitar o rastreamento de modificações de objetos
db.init_app(app)

# Rota para criar as tabelas no banco de dados
#@app.route('/criar_tabelas')
#def criar_tabelas():
    #db.create_all()  # Cria todas as tabelas definidas no modelo
    #return "Tabelas criadas com sucesso!"

# Rota para a página principal ("/")
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Recebe os dados do formulário
        nome = request.form.get("nome")
        idade = request.form.get("idade")
        
        nome = nome.title()
        
        # Cria uma nova pessoa no banco de dados
        nova_pessoa = Pessoa(nome=nome , idade=int(idade))
        db.session.add(nova_pessoa)
        db.session.commit()
        
        return redirect(url_for("home"))  # Redireciona de volta à página inicial

    # Rota GET exibe a lista de pessoas cadastradas
    pessoas = Pessoa.query.all()
    return render_template("cadastro_de_pessoa.html", pessoas=pessoas)

# Rota para deletar uma pessoa
@app.route("/deletar/<int:id_pessoa>")
def deletar(id_pessoa):
    pessoa = Pessoa.query.get(id_pessoa)
    if pessoa:
        db.session.delete(pessoa)
        db.session.commit()
    return redirect(url_for("home"))

# Rota para cadastro de transação
@app.route("/cadastro_transacao", methods=["GET", "POST"])
def cadastro_transacao():
    pessoas = Pessoa.query.all()
    transacoes = Transacao.query.all()
    if request.method == "POST":
        
        descricao = request.form["descricao"]
        valor = float(request.form["valor"])
        tipo = request.form["tipo"]
        id_pessoa = int(request.form["id_pessoa"])
        
        usuario_atual= Pessoa.query.filter(Pessoa.id_pessoa==id_pessoa).first()
        if usuario_atual.idade < 18 and tipo=="Receita":
            return redirect(url_for("cadastro_transacao", error="A pessoa deve ter mais de 18 anos para registrar uma Receita."))
        
        
        # Cria uma nova transação
        nova_transacao = Transacao(
            descricao=descricao, 
            valor=valor, 
            tipo=tipo, 
            id_pessoa=id_pessoa
        )
        db.session.add(nova_transacao)
        db.session.commit()

        return redirect(url_for("cadastro_transacao"))

    # No método GET, exibe o formulário com a lista de pessoas e transações

    
    return render_template("cadastro_de_transacoes.html", pessoas=pessoas, transacoes=transacoes)

# Rota para calcular totais por pessoa
@app.route('/totais_por_pessoa')
def totais_por_pessoa():
    pessoas = Pessoa.query.all()
    
    resultados = []
    
    for pessoa in pessoas:
        total_receitas = db.session.query(func.sum(Transacao.valor)).filter(Transacao.id_pessoa == pessoa.id_pessoa, Transacao.tipo == 'Receita').scalar() or 0
        total_despesas = db.session.query(func.sum(Transacao.valor)).filter(Transacao.id_pessoa == pessoa.id_pessoa, Transacao.tipo == 'Despesa').scalar() or 0
        saldo = total_receitas - total_despesas
        resultados.append({
            'nome': pessoa.nome,
            'total_receitas': total_receitas,
            'total_despesas': total_despesas,
            'saldo': saldo
        })

    return render_template('totais_por_pessoa.html', resultados=resultados)

# Rota para calcular totais gerais
@app.route('/totais_gerais')
def totais_gerais():
    total_receitas = db.session.query(func.sum(Transacao.valor)).filter(Transacao.tipo == 'Receita').scalar() or 0
    total_despesas = db.session.query(func.sum(Transacao.valor)).filter(Transacao.tipo == 'Despesa').scalar() or 0
    saldo_geral = total_receitas - total_despesas

    return render_template('totais_gerais.html', total_receitas=total_receitas, total_despesas=total_despesas, saldo_geral=saldo_geral)

if __name__ == "__main__":
    app.run(debug=True)
