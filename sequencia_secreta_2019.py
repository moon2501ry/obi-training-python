# https://olimpiada.ic.unicamp.br/pratique/pj/2019/f1/secreta/

numbers = int(input());
coluna = [];
circulos = [];

for _ in range(0, numbers):
    coluna.append(int(input()));

for i in range(0,len(coluna)):
    if i == 0:
        circulos.append(coluna[i]);
    else:
        if coluna[i] != circulos[-1]:
            circulos.append(coluna[i]);

print(len(circulos));