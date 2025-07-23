# https://olimpiada.ic.unicamp.br/pratique/pj/2010/f1/garcom/

n_bandeijas = int(input());
copos_quebrados = 0;

for _ in range(0,n_bandeijas):
    n_latas, n_copos = map(int, input().split());
    if n_latas > n_copos:
        copos_quebrados += n_copos;

print(copos_quebrados);