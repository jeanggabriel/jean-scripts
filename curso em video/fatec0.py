import os
print ('.::Programa Prnto Para Ser Ultilizado::.')

while True:
    print ('<::SISTEMA DE FINANCIAMENTO::>')
    marca = input('.::Digite a marca do carro::.')
    modelo = input('.::Digite o modelo do carro::.')
    carro = float(input('.::Digite o valor do carro::.R$'))
    salario = float(input('.::Digite o salario do comprador::.R$'))
    anos = int(input('.::Em quantos anos deseja fazer o  financiamento?::.'))
    prestaçao = carro / (anos * 12) # conta q paga em anos
    minimo = salario * 30 / 100 #Conta que equivale a 30% do salario do usuário.
    print ('para pagar uma carro da marca', marca, 'do modelo', modelo, 'De R$ {:.2f} em {} anos a '.format (carro, anos), end = '')
    print ('prestaçao sera de R$ {:.2f}'.format (prestaçao))
if prestaçao <= minimo:
    print ('< O emprestimo pode ser concedido >')
else:
    print('< Emprestimo Negado >')
if anos > 5:
    print('.::PORÉM VOCE NÃO PODE FINANCIAR POR MAIS DE 5 ANOS, POIS NOSSA EMPRESA NÃO PERMITE ::.')
    opcao2 = input('Deseja tentar acima de 5 anos, porem com juros? [1/2]')
if opcao2 == '2':
    system(exit)
def juros_t(t, n, amortizacao, taxa):
    return (n - t + 1) * amortizacao * taxa
    principal = float ( input ("1. Informe o valor a ser financiado: "))
    os.system("clear")
    n = int ( input ("2. Informe o prazo de quitação do financiamento (em meses): "))
    os.system("clear")
    taxa_juros_anual = float (input ("3. Informe a taxa de juros anual (em %): ")) / 100.0
    os.system("clear")
    amortizacao = principal / n
    taxa_juros_mensal = pow(1.0 + taxa_juros_anual, 1.0 / 12) - 1.0;
    print ("AMORTIZAÇÃO: R$ %.2f" % amortizacao)
    print ("VALOR DO FINANCIAMENTO: R$ %.2f\n\n" % principal)
    print ("\t FINANCIAMENTO = R$ %.2f \t MESES: %i meses \t TAXA: %i%% ano (%.f%%)" % (principal, n, taxa_juros_anual, taxa_juros_mensal))
    print ("\t","-"*80,"\n")
    print ("\t MÊS\tSALDO INICIAL\tPRESTAÇÃO\tAMORTIZAÇÃO\t  JUROS\tSALDO FINAL")
    print ("\t ---\t-------------\t---------\t-----------\t-------\t-----------")
    saldo_inicial = principal
for t in range(1, n + 1):
    saldo_final = saldo_inicial - amortizacao
    juros = juros_t(t, n, amortizacao, taxa_juros_mensal)
    prestacao = amortizacao + juros
    print ("\t%4.i\t%13.2f\t%9.2f\t%11.2f\t%7.2f\t%11.2f" % (t, saldo_inicial, prestacao, amortizacao, juros, saldo_final))
    saldo_inicial = saldo_final 
    opcao = input('Deseja repitir o proceso? [s/n]')
if opcao == 'n':
    SystemExit()