def inverter_string(string):

    caracteres = list(string)
    
    inicio = 0
    fim = len(caracteres) - 1
    
 
    while inicio < fim:
    
        caracteres[inicio], caracteres[fim] = caracteres[fim], caracteres[inicio]
        
 
        inicio += 1
        fim -= 1
    

    return ''.join(caracteres)

string_original = input("Digite uma string para inverter: ")


resultado = inverter_string(string_original)

# Exibe o resultado
print(f"String invertida: {resultado}")
