class FilaBase:
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual:str = None

    def reseta_fila(self)-> None:
            if self.codigo >= 200:
                self.codigo = 0
            else:
                self.codigo = int(self.codigo) + 1