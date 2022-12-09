
a = 'AAAAA'
b = 'BBBBBB'
c = 1.18546
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)
# a é argumento, nome1 é parâmetro
print(formato)