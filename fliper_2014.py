# https://olimpiada.ic.unicamp.br/pratique/pj/2014/f1/fliper/

_input = str(input()).split();
portilha_p = int(_input[0]);
portilha_r = int(_input[1]);
result = "";

match portilha_p:
    case 1:
        match portilha_r:
            case 1:
                result = "A";
            case 0:
                result = "B";
    case 0:
        result = "C";

print(result);