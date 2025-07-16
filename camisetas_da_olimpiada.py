num_premiados = int(input());
tamanhos_solicitados = str(input()).split();
num_camisas_p = int(input());
num_camisas_m = int(input());

for i in tamanhos_solicitados:
    match int(i):
        case 1:
            num_camisas_p -= 1;
        case 2:
            num_camisas_m -= 1;

if num_camisas_p < 0 or num_camisas_m < 0:
    print("N");
else:
    print("S");