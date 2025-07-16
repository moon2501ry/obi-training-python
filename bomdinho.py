# https://olimpiada.ic.unicamp.br/pratique/pj/2017/f1/bondinho/

n_alunos = int(input());
n_monitores = int(input());
max_cabine = 50;

if n_alunos + n_monitores > max_cabine:
    print("N");
else:
    print("S");