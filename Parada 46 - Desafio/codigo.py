# Função de conversão de centímetros para outras medidas
centimetros = float(input("Digite a medida em centímetros: "))

# Conversão centímetros para metros
def para_metros(valor):
    metros = valor / 100
    print(f"Metros: {metros:.2f} m")

# Conversão de centímetros para milímetros
def para_milimetros(valor):
    milimetros = valor * 10
    print(f"Milímetros: {milimetros:.2f} mm")

para_metros(centimetros)
para_milimetros(centimetros)