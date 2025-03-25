a = 'a)'
b = 'b)'
c = 1.1
string = '1 = {nome2} 2 = {nome1} 3 = {nome3:.2f} 4 = {nome1}'
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)