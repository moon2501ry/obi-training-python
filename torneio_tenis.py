# https://olimpiada.ic.unicamp.br/pratique/p1/2021/f1/torneio/
jogos = [];
grupo = -1;
for _ in range(0,6):
    jogos.append(str(input()));
vitorias = jogos.count("V");
if vitorias >= 5:
    grupo = 1;
elif vitorias <= 4 and vitorias >= 3:
    grupo = 2;
elif vitorias <= 2 and vitorias >= 1:
    grupo = 3;
print(grupo);
