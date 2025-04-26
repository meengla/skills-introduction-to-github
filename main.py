def eh_primo(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = input("Digite um número: ")
iteracao = 0  

while True:
    digitos = [int(d) for d in str(numero)]
    resultado = 0
    
    for i in range(len(digitos)):
        potencia = len(digitos) - 1 - i
        resultado += digitos[i] * (3 ** potencia)
    
    iteracao += 1  
    print(f"Iteração {iteracao}: {numero} → {resultado}")
    
    if eh_primo(resultado) or abs(resultado) < 10:
        print(f"\nFim após {iteracao} iterações!")
        print(f"Motivo: {resultado} é {'primo' if eh_primo(resultado) else 'um número de 1 dígito'}.")
        break
   
    numero = resultado