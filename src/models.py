from flask_sqlalchemy import SQLAlchemy
from __init__ import app

db = SQLAlchemy(app)

class Mensagens(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(40), nullable=False)
  assunto = db.Column(db.String(50), nullable=False)
  descricao = db.Column(db.String(150), nullable=False)