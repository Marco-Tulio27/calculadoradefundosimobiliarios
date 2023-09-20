decisao=''
while True:
     print('Vamos Calcular Fundos de investimentos \n')
     valor_cota=float(input('Digite o valor da cota: R$ '))
     quantidade_anos=int(input('Digite a quantidade de anos que deseja investir: '))
     quantidade_cotas=int(input('Qual quantidade de cotas deseja comprar: '))
     porcentagem_renda=int(input('Digite a porcentagem de juros que irá render ao mês: '))

     calculo= (valor_cota)/100*(porcentagem_renda) #calcula quanto irá render a parcela mensalmente
     mes_tot_investido= quantidade_anos*12 # vai converter o numero de anos em mes 
     total_conta=valor_cota*mes_tot_investido # calcula o valor total da conta sem renda
     novo_total=(valor_cota*quantidade_cotas)+calculo
     print ('O valor investido será de: R$', round(valor_cota*quantidade_cotas,2))
     for x in range(mes_tot_investido):        
          if x == 0:
               print('valor do primeiro mes: R$',round(valor_cota*quantidade_cotas,2))  # Valor inicial do investimento
          else:
           novo_total = novo_total + (novo_total * porcentagem_renda / 100)  # Atualiza o novo total com os juros
          

     print('Valor total ao final dos investimentos: R$',float(round(novo_total,2)))
     print('O rendimento foi totalizado em: R$',float(round(novo_total-(valor_cota*quantidade_cotas),2)))
     from time import sleep
     sleep(3)
     decisao=input('Deseaja continuar? S/N: ')
     decisao=decisao.upper()
     if decisao =='N':
          print('Até Breve...')
          sleep(2)
          break
     else:
          pass


          
     
     