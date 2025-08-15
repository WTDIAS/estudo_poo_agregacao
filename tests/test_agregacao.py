import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agregacao import Autor, Capitulo, Livro

#==============================
# classe Autor
#==============================
class TestAutor(unittest.TestCase):
    def setUp(self):
        self.nome = "Machado de Assis"
        self.nacionalidade = "Brasileira"
        self.autor = Autor(self.nome,self.nacionalidade)

    def test_autor_sucesso(self):
        # verifica se o retorno esta funcionando como deveria
        self.assertEqual( self.autor.nome, self.nome)
        self.assertEqual( self.autor.nacionalidade, self.nacionalidade)

    def test_autor_nome_falha(self):
        # verifica as várias possibilidades de falha com valores invalidos
        valores_invalidos = [""," ",123]
        for valor in valores_invalidos:
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    self.autor.nome = valor


    def test_auto_nacionalidade_falha(self):
        # verifica as várias possibilidades de falha com valores invalidos
        valores_invalidos = [""," ",123]
        for valor in valores_invalidos:
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):                    
                    self.autor.nacionalidade = valor
            

#==============================
# classe Capitulo
#==============================
class TestCapitulo(unittest.TestCase):

    def setUp(self):
        self.titulo = "Pueira em alto mar"
        self.num_paginas = 10
        self.capitulo = Capitulo( self.titulo, self.num_paginas)


    def test_capitulo_sucesso(self):
        # verifica se o retorno esta funcionando como deveria
        self.assertEqual( self.capitulo.titulo, self.titulo)
        self.assertEqual( self.capitulo.num_paginas, self.num_paginas)

    def test_capitulo_titulo_falha(self):
        # verifica as várias possibilidades de falha com valores invalidos
        valores_invalidos = [""," ",1,-1,0]
        for valor in valores_invalidos:
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    self.capitulo.titulo = valor


    def test_capitulo_num_paginas(self):
        # verifica as várias possibilidades de falha com valores invalidos
        valores_invalidos = [""," ",-1,0]
        for valor in valores_invalidos:
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    self.capitulo.num_paginas = valor

        
#==============================
# classe Livro
#==============================
class TestLivro(unittest.TestCase):
    
    def setUp(self):        
        self.titulo = "Python na prática"
        self.ano_publicacao = 2021
        self.livro = Livro(self.titulo, self.ano_publicacao)
        self.autor_valido = Autor("Waldir Souza", "Brasileira")
        self.capitulo_valido = Capitulo("POO com Python", 10)
    
    def test_livro_sucesso(self):
        # verifica se o retorno esta funcionando como deveria
        self.assertEqual(self.livro.titulo,self.titulo)
        self.assertEqual(self.livro.ano_publicacao,self.ano_publicacao)

    def test_livro_titulo_falha(self):
        # verifica as várias possibilidades de falha com valores invalidos
        valores_invalidos = [""," ",123]
        for valor in valores_invalidos:
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    self.livro.titulo = valor

    def test_livro_ano_publicação(self):
        # verifica as várias possibilidades de falha com valores invalidos
        valores_invalidos = [""," ",999,-1,0]
        for valor in valores_invalidos:
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    self.livro.ano_publicacao = valor

    # Testes para cadastrar_autores
    def test_cadastrar_autor_valido(self):
        #verifica se o metodo cadastrar autoresesta funcionando como esperado
        self.livro.cadastrar_autores(self.autor_valido)
        self.assertIn(self.autor_valido, self.livro.autores)

    def test_cadastrar_autor_invalido(self):
        #verifica que irá dar falha ao cadastrar autor com valor inválido
        with self.assertRaises(ValueError) as contexto:
            self.livro.cadastrar_autores("Não é um autor")
        self.assertEqual(str(contexto.exception), "O autor deve ser um objeto do tipo Autor.")

    # Testes para cadastrar_capitulo
    def test_cadastrar_capitulo_valido(self):
        #verifica se o metodo cadastrar capitulo esta funcionando como esperado
        self.livro.cadastrar_capitulo(self.capitulo_valido)
        self.assertIn(self.capitulo_valido, self.livro.capitulos)

    def test_cadastrar_capitulo_invalido(self):
        #verifica que irá dar falha ao cadastrar capitulo com valor inválido
        with self.assertRaises(ValueError) as contexto:
            self.livro.cadastrar_capitulo(["lista", "inválida"])
        self.assertEqual(str(contexto.exception), "O capítulo deve ser um objeto do tipo Capítulo.")





if __name__ == "__main__":
    unittest.main()