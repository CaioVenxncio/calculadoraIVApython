# Adicionar IVA ( Imposto sobre Valor Agregado )
def adicionar_iva():
    Iva = float(input('\nInsira o Imposto sobre Valor Agregado: '))
    Valor_liquido = float(input('Insira o valor líquido do produto: '))
    
    Iva = (Iva * Valor_liquido) / 100
    Valor_bruto = Iva + Valor_liquido
    Imposto = Valor_bruto - Valor_liquido
    
    print("\n============================================================")
    print('\nSeu Imposto sobre Valor Agregado (IVA): R$ {:,.2f}'.format(Imposto))
    print('Preço líquido: R$ {:,.2f}'.format(Valor_liquido))
    print('Preço bruto: R$ {:,.2f}'.format(Valor_bruto))

# Retirar IVA ( Imposto sobre Valor Agregado )
def remover_iva():
    Iva = float(input('\nInsira o Imposto sobre Valor Agregado: '))
    Valor_bruto = float(input('Insira o valor bruto do produto: '))
    
    Valor_liquido = Valor_bruto / (1 + (Iva / 100))
    Imposto = Valor_bruto - Valor_liquido
    print("\n============================================================")
    print('\nSeu Imposto sobre Valor Agregado (IVA): R$ {:,.2f}'.format(Imposto))
    print('Preço líquido: R$ {:,.2f}'.format(Valor_liquido))
    print('Preço bruto: R$ {:,.2f}'.format(Valor_bruto))

#criando opções
while True:  
    print("\n ========== MAIN MENU =========")  
    print("1. Adicionar IVA ( Imposto sobre Valor Agregado )")  
    print("2. Retirar IVA ( Imposto sobre Valor Agregado )")  
    print("3. Sair")  
    
    escolha = int(input("\nEscolha um das opções:"))  
  
    if escolha == 1:  

        print("\n====== Adicionar IVA ( Imposto sobre Valor Agregado ) ======") 
        
        # chamando a funcao adicionar IVA 
        adicionar_iva() 
        
    elif escolha == 2:  
        print("\n====== Retirar IVA ( Imposto sobre Valor Agregado ) ======")
        # chamando a funcao remover IVA 
        remover_iva()
      
    elif escolha == 3:  
        break  
    else:  
        print("\nOps! Escolha incorreta.")