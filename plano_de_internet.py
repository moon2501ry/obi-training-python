cota = int(input());
cota_inicial = cota;
n_meses = int(input());
list_meses = [];
meses_passados = 0;

while True:
    n_mes = int(input());
    if n_mes <= cota:
        cota = cota_inicial + (cota - n_mes);
    else:
        cota = cota_inicial;

    meses_passados += 1;

    if meses_passados >= n_meses:
        break;
print(cota);