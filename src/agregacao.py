# Estudo de POO com Python - Conceitos aprendidos:
#=================================================
# .Herança
# .Encapsulamento
# .Agregação
#=================================================

"""
OBS:
Observação: Embora este projeto utilize Agregação (onde Livro pode existir sem Autores ou Capítulos), 
eu observo que, em um caso real, seria mais adequado usar Composição, exigindo que o livro seja criado 
já com autores e capítulos.
"""

#====================================
# CLASSE AUTOR
#====================================
class Autor:
    def __init__(self, nome:str, nacionalidade:str) -> None:
        self.nome = nome
        self.nacionalidade = nacionalidade

    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome:str) -> None:
        if not isinstance(nome,str) or not nome.strip() or len(nome) < 3:
            raise ValueError("Infome um nome para o autor.")
        self._nome = nome

    @property 
    def nacionalidade(self) -> str:
        return self._nacionalidade
    
    @nacionalidade.setter
    def nacionalidade(self, nacinalidade:str) -> None:
        if  not isinstance(nacinalidade,str) or not nacinalidade.strip() or len(nacinalidade) < 3:
            raise ValueError("Informe a nacionalidade para o autor.")
        self._nacionalidade = nacinalidade

    def __str__(self):
        return f"Nome do autor: {self.nome} | Nacionalidade: {self.nacionalidade}"
    
#====================================
# CLASSE CAPITULO
#====================================
class Capitulo:
    def __init__(self, titulo:str, num_paginas:int):
        self.titulo = titulo
        self.num_paginas = num_paginas

    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor:str) -> None:
        if not isinstance(valor,str) or not valor.strip() or len(valor) < 3:
            raise ValueError("Informe titulo para o capítulo")
        self._titulo = valor
        
    @property
    def num_paginas(self) -> int:
        return self._num_paginas
    
    @num_paginas.setter
    def num_paginas(self, valor:int) -> None:
        if not isinstance(valor, int) or valor < 1:
            raise ValueError("Informe a quantidade de páginas para o capítulo")
        self._num_paginas = valor

    def __str__(self):
        return f"Titulo do capítulo: {self.titulo} | Quantidade de paginas: {self.num_paginas}"

#====================================
# CLASSE LIVRO
#====================================
class Livro:    
    def __init__(self, titulo:str, ano_publicacao:int) -> None:
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.autores = []
        self.capitulos = []

    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo:str) -> str:
        if not isinstance(titulo,str) or not titulo.strip() or len(titulo) < 3:
            raise ValueError("Informe título para o livro.")
        self._titulo = titulo

    @property
    def ano_publicacao(self) -> int:
        return self._ano_publicacao
    
    @ano_publicacao.setter
    def ano_publicacao(self, ano_publicacao:int) -> None:
        if not isinstance(ano_publicacao,int) or ano_publicacao < 1000:
            raise ValueError("Informe o ano de fabricação")
        self._ano_publicacao = ano_publicacao

    def cadastrar_autores(self, autor:Autor) -> None:
        if not isinstance(autor,Autor):
            raise ValueError("O autor deve ser um objeto do tipo Autor.")
        self.autores.append(autor)

    def cadastrar_capitulo(self, capitulo:Capitulo) -> None:
        if not isinstance(capitulo,Capitulo):
            raise ValueError("O capítulo deve ser um objeto do tipo Capítulo.")
        self.capitulos.append(capitulo)
    
    def __str__(self):        
        str_autores = ", ".join(str(autor) for autor in self.autores)
        str_capitulos = "\n -"+"\n -".join(str(capitulo) for capitulo in self.capitulos)
        return (
            f"Livro: {self.titulo} {self.ano_publicacao} \n"
            f"Autores: {str_autores} \n"
            f"Capítulos: {str_capitulos}"
        )

#====================================
# EXECUÇÃO
#====================================
if __name__ == "__main__":
    autor1 = Autor("Flavio Augusto","Brasileira")
    capitulo1 = Capitulo("O clique da confiança",5)
    capitulo2 = Capitulo("O bico",6)
    livro1 = Livro("Ponto de inflexão",2022)
    livro1.cadastrar_autores(autor1)
    livro1.cadastrar_capitulo(capitulo1) 
    livro1.cadastrar_capitulo(capitulo2)


    print(livro1)