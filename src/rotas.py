from flask import Flask, render_template, Blueprint, request, redirect
from models.mensagem import Mensagem
from db import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html', titulo="Home")

@main.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo="Sobre")

@main.route('/contato', methods = ['POST', 'GET'])
def contato():
  if request.method == 'POST':
    email = request.form['email']
    assunto = request.form['assunto']
    descricao = request.form['descricao']
    mensagem = Mensagem(email=email, assunto=assunto, descricao=descricao)
    db.session.add(mensagem)
    db.session.commit()
    return redirect('/mensagens')
  else:
    return render_template('contato.html', titulo="Contato")

@main.route('/mensagens')
def mensagens():
  return render_template('mensagens.html', titulo="Mensagens")