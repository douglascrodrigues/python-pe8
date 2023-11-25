from typing import Union

from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de fila não existe')

"""
    O metodo "pega_fila" pertence a classe FabricaFila, por padrão para
    para utilizar esse metodo, eu precisaria instanciar a classe FabricaFilas
    e após instanciado, chamar o metodo, porém, como ele é um @staticmethod, 
    isso não é mais necessario.
"""
