from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Sara', idade=10)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome='Samara').first()
    # print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Samara').first()
    pessoa.idade = 21
    pessoa.save()
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Hurtado').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()
def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)
if __name__ == '__main__':
    insere_usuario('Samara', '1879')
    insere_usuario('Sara', '123')
    consulta_todos_usuarios()
    # altera_pessoa()
    # insere_pessoas()
    # consulta_pessoas()