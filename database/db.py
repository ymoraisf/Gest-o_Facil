from database import db

class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    categoria = db.Column(db.String(50))
    quantidade = db.Column(db.Integer)
    preco = db.Column(db.Float)

    vendas = db.relationship('Venda', backref='produto')

class Venda(db.Model):
    __tablename__ = 'vendas'

    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'))
    valor = db.Column(db.Float)
    data = db.Column(db.String(20))