# Read & Write

# input
# string "LW" + limite de operações simultâneas de read

# passo 1 --> ler string
# passo 2 --> ler limite 

# output --> número de operações mínimas

entrada = str(input())
limite_r = int(input())
n_operacoes = entrada.count("W")

if "R" in entrada:
    if entrada.count("R") % limite_r != 0:
        n_operacoes += entrada.count("R") // limite_r + 1
    else:
        n_operacoes += entrada.count("R") / limite_r

for p, v in enumerate(entrada):
    print(f"{p}o --> {v}")
    if v == "R" and entrada[p + 1] == "R":
        if numero_rs < limite_r:
            numero_rs += 1
        else:
            n_operacoes += 1
            numero_rs = 0
    else:
        n_operacoes += 1

print(n_operacoes)

