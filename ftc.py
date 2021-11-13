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

