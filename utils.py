from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Hurtado', idade=20)
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
if __name__ == '__main__':
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()