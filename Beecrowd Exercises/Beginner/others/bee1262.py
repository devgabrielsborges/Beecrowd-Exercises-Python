# Read & Write

# input
# string "LW" + limite de operações simultâneas de read

# passo 1 --> ler string
# passo 2 --> ler limite 

# output --> número de operações mínimas

rw_input = str(input())   # input inicial
r_limit = int(input())    # limite de R's
operations_counter = rw_input.count("W")   # contador de operações mínimas considerando um input com apenas W

# bloco consideranndo apenas R no input
if "R" in rw_input and "W" not in rw_input:
    if rw_input.count("R") % r_limit != 0:
        operations_counter += rw_input.count("R") // r_limit + 1
    else:
        operations_counter += rw_input.count("R") / r_limit

# bloco considerando R e W no input
elif "R" in rw_input and "W" in rw_input:
    operations_counter = 0 # contabiliza o número de operações 
    r_counter = 0   # contabiliza "R" para não exceder o limite
    for k, v in enumerate(rw_input):   # Key and Value
        if v == "W":
            r_counter = 0
            operations_counter += 1
        elif v == "R":
            try:
                if r_counter == 0:  # contabilizando primeiro R
                    r_counter += 1
                if rw_input[k + 1] == "R" and r_counter < r_limit:
                    r_counter += 1
                else:
                    r_counter = 0
                    operations_counter += 1
            except:
                if r_counter == r_limit:
                    r_counter = 0
                    operations_counter += 1
                else:
                    operations_counter += 1
print(operations_counter)

