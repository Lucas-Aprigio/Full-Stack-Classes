from app import bd, login
from flask_login import UserMixin, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(UserMixin, bd.Model):
    __tablename__ ='usuarios'
    id = bd.Column('id', bd.Integer(), primary_key=True, autoincrement=True)
    nome_completo=bd.Column('nomeCompleto', bd.String(40), nullable=False)
    email=bd.Column('email', bd.String(70), nullable=False)
    senha_hash=bd.Column('senha_hash', bd.String(128), nullable=False)

    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)
    
    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

@login.user_loader
def user_loader(email):
    return Usuario.query.get(str(email))

