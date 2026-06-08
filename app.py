from flask import Flask, render_template, request, redirect, url_for
from database import db
from database.db import Produto, Venda

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gestao.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    produtos = Produto.query.all()
    vendas = Venda.query.all()

    return render_template(
        'dashboard.html',
        produtos=produtos,
        vendas=vendas
    )


@app.route('/cadastro-produto', methods=['GET', 'POST'])
def cadastro_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        quantidade = int(request.form['quantidade'])
        preco = float(request.form['preco'])

        novo_produto = Produto(
            nome=nome,
            categoria=categoria,
            quantidade=quantidade,
            preco=preco
        )

        db.session.add(novo_produto)
        db.session.commit()

        return redirect(url_for('dashboard'))

    return render_template('cadastro_produto.html')


@app.route('/produto/editar/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    produto = Produto.query.get_or_404(id)

    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.categoria = request.form['categoria']
        produto.quantidade = int(request.form['quantidade'])
        produto.preco = float(request.form['preco'])

        db.session.commit()

        return redirect(url_for('dashboard'))

    return render_template('editar_produto.html', produto=produto)


@app.route('/produto/excluir/<int:id>')
def excluir_produto(id):
    produto = Produto.query.get_or_404(id)

    db.session.delete(produto)
    db.session.commit()

    return redirect(url_for('dashboard'))


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)