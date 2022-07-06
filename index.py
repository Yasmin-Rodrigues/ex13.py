#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ãngulo
from math import radians, cos, tan, sin
a =float(input('Digite o ângulo que deseja:'))
seno =sin(radians(a))
print('O ângulo de {} tem o SENO de {:.2f}' .format(a, seno))
cosseno =cos(radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}' .format(a, cosseno))
tang =tan(radians(a))
print('O ângulo de {} tem a TANGENTE de {:.2f}' .format(a, tang))
