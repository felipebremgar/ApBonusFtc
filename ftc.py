# casos de teste
# valido: 159.200.335-41 012.690.402-27 2011.11.11 17:18:30 [14.40,13.30,14.40,155.60] 658214793-ta8ux-822
#         277.781.070-23 39.900.653/0001-62 2016.02.29 22:33:11 [3.00,4.00,12.00] 746985321-pof32-000-111
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

def valida_cpf(entrada):
	validation = re.match(cpf_regex,entrada)
	if validation == None:
		try:
			if valida_formato_cpf(entrada) == True:
				print('True')
			else:
				print('False')
		except:
			print('False')
	else:
		entrada = re.sub("\.", "", entrada, 2)
		entrada = re.sub("\-", "", entrada, 1)
		
		if valida_formato_cpf(entrada) == False:
			print('False')
		else:
			print('True')    

def valida_formato_cpf(entrada):
    if len(entrada) < 11:
        return False
    if entrada in [s * 11 for s in [str(n) for n in range(10)]]:
        return False
    
    calc = lambda t: int(t[1]) * (t[0] + 2)
    d1 = (sum(map(calc, enumerate(reversed(entrada[:-2])))) * 10) % 11
    d2 = (sum(map(calc, enumerate(reversed(entrada[:-1])))) * 10) % 11
    return str(d1) == entrada[-2] and str(d2) == entrada[-1]

cpf_regex  = "^\d{3}\.\d{3}\.\d{3}\-\d{2}$"


entrada = input()
valida_cpf(entrada)
