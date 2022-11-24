from db import db

class Mensagem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, nullable=False)
  assunto = db.Column(db.String, nullable=False)
  descricao = db.Column(db.String, nullable=False)