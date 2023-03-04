import matplotlib.pyplot as plt

# Dados para os eixos x e y e tamanho do vetor

n = 1000
x = [0,1]
fibonacci = [0,1]

# Fazendo Fibonacci

for i in range(2,n):    
    val_carregado = fibonacci[i-1]
    val_carregado2 = fibonacci[i-2]
    fibonacci.append(val_carregado + val_carregado2)
    x.append(i)

phi = fibonacci[-1]/fibonacci[-2]
print(phi)

# print(fibonacci)
# print(x)

# # Plotando o gráfico
# plt.plot(x, fibonacci)

# # Definindo os títulos dos eixos
# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')

# # Exibindo o gráfico
# plt.show()
