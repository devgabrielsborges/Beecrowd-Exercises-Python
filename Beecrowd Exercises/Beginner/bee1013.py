values_str = input().split()

a = int(values_str[0])
b = int(values_str[1])
s = int(values_str[2])

values = [a, b, s]
valores = sorted(values, reverse=True)

print(f'{valores[0]} eh o maior')