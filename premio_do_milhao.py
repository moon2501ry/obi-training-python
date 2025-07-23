# https://olimpiada.ic.unicamp.br/pratique/pj/2015/f1/premio/

n_dias = int(input());
acessos = 0;
dias = 0;

for _ in range(0,n_dias):
    if acessos < 1000000:
        acessos += int(input());
        dias += 1;
    else:
        break;

print(dias);