valores = input().split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

print(f'TRIANGULO: {(A * C / 2):.3f}\n'
      f'CIRCULO: {((C**2 * 3.14159)):.3f}\n'
      f'TRAPEZIO: {((A+B) * C / 2):.3f}\n'
      f'QUADRADO: {(B**2):.3f}\n'
      f'RETANGULO: {(A*B):.3f}')
