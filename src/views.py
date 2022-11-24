from flask import render_template, redirect, request
from __init__ import app
from models import db, Mensagens

@app.route('/')
def home():
    return render_template('index.html', titulo="Home")

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo="Sobre")

@app.route('/contato', methods = ['POST', 'GET'])
def contato():
  if request.method == 'POST':
    email = request.form['email']
    assunto = request.form['assunto']
    descricao = request.form['descricao']
    mensagens = Mensagens(id=0, email=email, assunto=assunto, descricao=descricao)
    db.session.add(mensagens)
    db.session.commit()
    return redirect('/mensagens')
  else:
    return render_template('contato.html', titulo="Contato")

@app.route('/mensagens')
def mensagens():
    mensagens = Mensagens.query.all()
    return render_template('mensagens.html', titulo="Mensagens", mensagens=mensagens)