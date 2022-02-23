from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError
from werkzeug.urls import url_parse
from forms import LoginForm, SignupForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SECRET_KEY']='segredo'
bd = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

from models import Usuario
bd.create_all()



@app.route('/calculaflask', methods=['POST'])
def calculaflask():
    n1=float(request.form['n1'])
    n2=float(request.form['n2'])
    operation=request.form['operation']

    if operation == "soma":
        resultado = int(n1) + int(n2)
    elif operation == "sub":
        resultado = int(n1) - int(n2)
    elif operation == "mult":
        resultado = int(n1) * int(n2)
    elif operation == "div":
        resultado = int(n1) / int(n2)
    else:
        resultado = "Operação não suportada"
    
    return render_template(
        'index.html',
        n1=n1,
        n2=n2,
        operation=operation,
        resultado=resultado
    )   

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template('index.html')
    form=LoginForm()
    
    print(form.validate_on_submit())
    if form.validate_on_submit():
        usuario=Usuario.query.filter(Usuario.email==form.email.data).first()
        print(usuario)
        if usuario is not None and usuario.check_senha(form.senha.data):    
            login_user(usuario)
            proxima_pagina= request.args.get('next')
            if not proxima_pagina or url_parse(proxima_pagina).netloc!="":
                return redirect('/index.html')
            return redirect(proxima_pagina)
        form.error = "Usuario ou senha inválidos"  
    return render_template('/login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login.html')
  
@app.route('/')
@app.route('/index.html')
@login_required
def index():
    usuarios=Usuario.query.all()
    return render_template('/index.html',usuarios=usuarios)

@app.route('/registrar.html', methods=['GET', 'POST'])
def registrarusuario():
    if current_user.is_authenticated:
        return render_template('/index.html')
    form = SignupForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
       
        try:
            usuario=Usuario(nome_completo=form.nome.data,   
                        email=form.email.data)
            usuario.set_senha(senha=form.senha.data)
            
            bd.session.add(usuario)
            bd.session.commit()
            return render_template("/registrar.html", form=form)
        except IntegrityError:
            bd.session.rollback()
            erro= "Esse nome de usuário já esta em uso"
    return render_template('/registrar.html', form=form)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

