import abc
from typing import List

from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual:str = ''

    def inseri_cliente(self):
        self.fila.append(self.senha_atual)

    def reseta_fila(self)-> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    @abc.abstractclassmethod
    def gera_senha_atual(self):
        ...

    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    @abc.abstractclassmethod
    def chama_cliente(self, caixa:int) -> str:
        ...

"""
    Quando importarmos a classe FilaBase, determinamos que os metodos gera_senha, 
    atualiza_senha, chama_cliente sejam utilizados, por isso criamos a classe abstrata

    TemplateMethod

    Em uma classe abstrada, a sua filha (quem herda a abstrata), os metodos herdados
    necessita ser sobrescrito nas classes filhas, devido as regras serem diferentes.

    FactoryMethod


"""
