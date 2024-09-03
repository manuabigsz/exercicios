def pertence_fibonacci(n):
   
    a, b = 0, 1
    
   
    if n == 0 or n == 1:
        return True
    
   
    while b < n:
        a, b = b, a + b
    

    return b == n


numero = int(input("Informe um número: "))

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
