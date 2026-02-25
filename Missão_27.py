

numero = int(input("Digite um número: "))


if numero % 2 == 0:
    
    
    if numero % 3 == 0:
        
        
        if numero >= 10 and numero <= 30:
            print("✅ O cofre abriu!")
        else:
            print(" Cofre bloqueado! Número fora do intervalo.")
    
    else:
        print(" Cofre bloqueado! Não é múltiplo de 3.")

else:
    print(" Cofre bloqueado! Não é número par.")