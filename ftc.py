# casos de teste
# valido: 159.200.335-41 012.690.402-27 2011.11.11 17:18:30 [14.40,13.30,14.40,155.60] 658214793-ta8ux-822
#         277.781.070-23 39.900.653/0001-62 2016.02.29 22:33:11 [3.00,4.00,12.00] 746985321-pof32-000-111
# invalido: 573.294.590-000 260.382.860-63 2018.03.13 14:09:59 [600.00] 666333999-bcd45-246-000
#           39.900.653/0001-62            

import re
cpf_regex  = "^\d{3}\.\d{3}\.\d{3}\-\d{2}$"
data_regex = "([12]\d{3}.(0[1-9]|1[0-2]).(0[1-9]|[12]\d|3[01]))"
hour_regex = "^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$"
cnpj_regex = "\d{2}\.?\d{3}\.?\d{3}\/?\d{4}\-?\d{2}"

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

def valida_cod_transacao (cod):
    cod_transacao = cod.split("-")
    match1 = re.search(r"[0-9]{9}",cod_transacao[0])
    match2 = re.search(r"(?!([a-z0-9])*.*\1)([a-z0-9]){5}",cod_transacao[1])
    match3 = re.search(r"([02468]){3}",cod_transacao[2])
    try:
        match4 = re.search(r"([01]){3}",cod_transacao[3])
        if (match1 and match2 and match3 and match4):
            return True
        else:
            return False
    except:
        if (match1 and match2 and match3):
            return True
        else:
            return False

def valida_data(entrada):
    validacao = re.match(data_regex, entrada)
    if len(entrada) != 0:
        if validacao:
            print ('True')
        else:
            print ('False')
    else:
        print ('Error')

def valida_hora(entrada):
    validacao = re.match(hour_regex, entrada)
    if len(entrada) != 0:
        if validacao:
            return ('True')
        else:
            return ('False')
    else:
        print ('Error')

def valida_formato_cnpj(entrada):
    validacao = re.match(cnpj_regex, entrada)
    if len(entrada) != 0:
        if validacao:
            return ('True')
        else:
            return ('False')
    else:
        print ('Error')

def valida_cnpj(entrada):
    validation = re.match(cnpj_regex,entrada)
    cnpj = re.sub(r'[^0-9]', '', entrada)
    if (valida_formato_cnpj != True):
        raiz_cnpj = cnpj[0:12]
        digito_ver = cnpj[12:14]

        ver = int(raiz_cnpj[0])*5
        ver += int(raiz_cnpj[1])*4
        ver += int(raiz_cnpj[2])*3
        ver += int(raiz_cnpj[3])*2
        ver += int(raiz_cnpj[4])*9
        ver += int(raiz_cnpj[5])*8
        ver += int(raiz_cnpj[6])*7
        ver += int(raiz_cnpj[7])*6
        ver += int(raiz_cnpj[8])*5
        ver += int(raiz_cnpj[9])*4
        ver += int(raiz_cnpj[10])*3
        ver += int(raiz_cnpj[11])*2

        ver_resto = ver % 11

        digito_1 = 0

        if ver_resto < 2:
            digito_1 = 0
        else:
            digito_1 = 11-ver_resto

        ver = int(raiz_cnpj[0])*6
        ver += int(raiz_cnpj[1])*5
        ver += int(raiz_cnpj[2])*4
        ver += int(raiz_cnpj[3])*3
        ver += int(raiz_cnpj[4])*2
        ver += int(raiz_cnpj[5])*9
        ver += int(raiz_cnpj[6])*8
        ver += int(raiz_cnpj[7])*7
        ver += int(raiz_cnpj[8])*6
        ver += int(raiz_cnpj[9])*5
        ver += int(raiz_cnpj[10])*4
        ver += int(raiz_cnpj[11])*3
        ver += digito_1 * 2

        ver_resto = ver % 11

        digito_2 = 0

        if ver_resto < 2:
            digito_2 = 0
        else:
            digito_2 = 11-ver_resto
            
        digito_calc = str(digito_1) + str(digito_2)

        if digito_calc == digito_ver:
            print('True')
        else:
            print('False')
    else: print ("False")

def valida_preco(entrada):
    match = re.search(r"^\[([0-9]+.[0-9]{2})(,([0-9])+.([0-9]){2})*\]$", entrada)
    print (match)
    if match:
        return True
    else:
        return False

# def valida_cnpj(entrada):
entrada = input()
valida_cnpj(entrada)