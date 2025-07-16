idade_monica = int(input());
idade_filho_a = int(input());
idade_filho_b = int(input());
idade_filho_c = idade_monica - idade_filho_a - idade_filho_b;

_list = [idade_filho_a, idade_filho_b, idade_filho_c];
_list.sort();
print(_list[2]);