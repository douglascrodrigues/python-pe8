from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria


fila_teste_2 = FilaPrioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(10))
print(fila_teste_2.chama_cliente(1))
print(fila_teste_2.estatistica('10/01/1993', 215, 'detail'))

"""
    lib mypy, ele valida o tipo da variavel ou parametro,
    conforme passado nos typeshint.
"""
