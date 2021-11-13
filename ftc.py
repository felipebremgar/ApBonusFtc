# casos de teste
# valido: 159.200.335-41 012.690.402-27 2011.11.11 17:18:30 [14.40,13.30,14.40,155.60] 658214793-ta8ux-822
# invalido: 573.294.590-000 260.382.860-63 2018.03.13 14:09:59 [600.00] 666333999-bcd45-246-000
import re

def trata_entrada(entrada):
    tratada = entrada.split(" ") 
    cpf_comprador = tratada[0]
    cpf_cnpj_vendedor = tratada[1]
    data = tratada[2]
    hora = tratada[3]
    precos = tratada[4]
    cod_transacao = tratada[5]

    return tratada

def codtransacao (cod):
    cod_transacao = cod.split("-")
    match1 = re.search(r"[0-9]{9}",cod_transacao[0])
    match2 = re.search(r"(?!([a-z0-9])*.*\1)([a-z0-9]){5}",cod_transacao[1])
    match3 = re.search(r"([02468]){3}",cod_transacao[2])
    try:
        match4 = re.search(r"([01]){3}",cod_transacao[3])
        if (match1 and match2 and match3 and match4):
            return ("True match4")
        else:
            return ("False match4")
    except:
        if (match1 and match2 and match3):
            return ("True match3")
        else:
            return ("False match3")