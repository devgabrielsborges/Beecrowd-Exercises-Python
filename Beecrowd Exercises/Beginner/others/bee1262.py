# Read & Write

# input
# string "LW" + limite de operações simultâneas de read

# passo 1 --> ler string
# passo 2 --> ler limite 

# output --> número de operações mínimas

entrada = str(input())
limite_r = int(input())
n_operacoes, numero_rs = 0, 0

for p, v in enumerate(entrada):
    print(p == int())
    print(f"{p}o --> {v}")
    prox = int(p + 1 if (p + 1) < len(entrada) else p)   # proximo valor recebe p + 1 se não for o último valor, senão --> p = p
    print(f"prox = int? --> {prox == int()} --- prox = {prox} --> {type(prox)}")
    if v == "R" and entrada[prox] == "R":
        if numero_rs < limite_r and prox != len(entrada):
            numero_rs += 1
            print(f"N Rs --> {numero_rs}")
        else:
            print("Limite alcançado")
            n_operacoes += 1
            numero_rs = 0
    else:
        print("Foi W")
        n_operacoes += 1
        numero_rs = 0
    print(n_operacoes + 1)

