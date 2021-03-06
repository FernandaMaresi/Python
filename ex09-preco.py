#-*-coding:utf8;-*-
#qpy:console

print('================================')
n = int(input('Qual o valor do produto?'))
novoValor = n - (n * 5/100)
print('======= Desconto de 5% ======')
print('O novo preço com desconto e {}'.format(novoValor))
print('=============================')
