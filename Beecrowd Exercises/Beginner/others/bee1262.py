# Read & Write

# input
# string "LW" + limite de operações simultâneas de read

# passo 1 --> ler string
# passo 2 --> ler limite 

# output --> número de operações mínimas

entrada = str(input())
limite_r = int(input())
n_operacoes = entrada.count("W")

if "R" in entrada and "W" not in entrada:
    if entrada.count("R") % limite_r != 0:
        n_operacoes += entrada.count("R") // limite_r + 1
    else:
        n_operacoes += entrada.count("R") / limite_r
elif "R" in entrada and "W" in entrada:
    n_operacoes = 0 # contabiliza o número de operações 
    numero_rs = 0   # contabiliza "R" para não exceder o limite
    for k, v in enumerate(entrada):
        prox = int(k + 1 if (k + 1) < len(entrada) else k) # proximo valor de verificação recebe k + 1 se não for o último valor, senão prox --> k
        if v == "R" and entrada[prox] == "R":
            if numero_rs < limite_r and prox < len(entrada):
                numero_rs += 1
        else:
            n_operacoes += 1
            numero_rs = 0
    n_operacoes += 1
    
print(n_operacoes)

