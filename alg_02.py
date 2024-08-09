ca = (float(input('Digite qual é o valor do cateto adjacente do triângulo retângulo para calcular a hipotenusa: ')))
co = (float(input('Digite qual é o valor do cateto oposto do triângulo retângulo: ')))
hip1 = (ca**2 + co**2)
import math
hip2 = math.sqrt(hip1)
print(f' O valor da hipotenusa é: {hip2}')
#Teorema de Pitágoras(Hipotenusa)