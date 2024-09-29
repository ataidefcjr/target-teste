def fibonacci(input):
    fib = [0, 1]
    while fib[-1] < input:
        fib.append(fib[-1] + fib[-2])
    print("\nSequencia de Fibonacci: ", fib,"\n")
    return fib

def verifica_fibonacci(numero_escolhido):
    sequencia = fibonacci(numero_escolhido)
    if numero_escolhido in sequencia:
        return f"O número {numero_escolhido} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero_escolhido} não pertence à sequência de Fibonacci."


numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

resultado = verifica_fibonacci(numero)
print(resultado)